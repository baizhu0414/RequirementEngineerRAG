from nltk.tokenize import sent_tokenize # 依赖nltk的punkt包
from langchain.schema import Document # 封装句子
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import pdfplumber
from bs4 import BeautifulSoup
import chardet

import os
import shutil
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

"""
编码文件到数据库。
"""

def delete_directory(directory):
    # 确保指定目录存在
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
        print(f"已删除目录及其内容: {directory}")
    else:
        print(f"目录不存在: {directory}")

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

# 用于从PDF中提取文本
def extract_text_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_html(filepath):
    encoding = detect_encoding(filepath)
    with open(filepath, 'r', encoding=encoding, errors='ignore') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return soup.get_text()

# 用于从TXT中读取文本
def extract_text_from_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def split_and_filter_paragraphs(text, min_length=10):
    """
    按照段落划分文本，并删除长度小于 min_length 的段落
    """
    # 按段落划分文本（假设段落是由换行符隔开的）
    paragraphs = text.split('\n')
    # 过滤掉长度小于 min_length 的段落
    filtered_paragraphs = [para for para in paragraphs if len(para.strip()) >= min_length]
    return filtered_paragraphs

import re

def split_and_merge_paragraphs(text, chunk_size=256):
    """
    将文本通过换行替换为空格，按数字+'.'句号划分段落，并合并小于chunk_size的段落。
    """
    # 将所有换行符替换为空格
    text = text.replace("\n", " ")

    # 使用正则表达式按数字+'.'划分段落
    paragraphs = re.split(r'(?=\d+\.)', text)

    # 清理每个段落的首尾空格
    paragraphs = [para.strip() for para in paragraphs if para.strip()]

    # 合并长度小于 chunk_size 的段落
    merged_paragraphs = []
    current_paragraph = ""

    for para in paragraphs:
        if len(current_paragraph) < chunk_size:
            current_paragraph += (" " if current_paragraph else "") + para
        else:
            if current_paragraph:
                merged_paragraphs.append(current_paragraph.strip())
            current_paragraph = para

    # 添加最后一个段落
    if current_paragraph:
        merged_paragraphs.append(current_paragraph.strip())

    return merged_paragraphs



# 读取目录下的所有文件并提取文本
def extract_text_from_dir(directory):
    documents = []
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1].lower()
            
            if ext == "pdf":
                text = extract_text_from_pdf(filepath)
            elif ext == "txt":
                text = extract_text_from_txt(filepath)
            elif ext in ["htm", "html"]:
                text = extract_text_from_html(filepath)
            else:
                continue  # 如果是其他格式的文件，跳过

            # 分割文本为句子(经过测试，效果不好)
            # sentences = sent_tokenize(text)
            # 创建文档对象，假设每个句子作为一个文档
            # docs = [Document(page_content=sent,  metadata={"source": filename.split('.')[0].lower()}) for sent in sentences]
            # 按固定长度划分 
            paras = split_and_merge_paragraphs(text)
            docs = [Document(page_content=paragraph,  metadata={"source": filename.split('.')[0].lower()}) for paragraph in paras]
            documents.extend(docs)

    return documents




dir="./content"
docs = extract_text_from_dir(dir)
# for i, doc in enumerate(docs):
#     if 0<=i<10 or 100<i<110 or 200<i<210 or 300<i<310:
#         print(doc.page_content, "===========\n")
#     else:
#         break

# 使用text2vec-large-chinese模型, 对上面chunk后的doc进行embedding。然后使用FAISS存储到向量数据库
embeddings=HuggingFaceEmbeddings(model_name="/root/autodl-tmp/text2vec-large-chinese", model_kwargs={'device': 'cuda'})
faiss_path = "/root/autodl-tmp/my_faiss_store.faiss"
if os.path.exists(faiss_path):
    delete_directory(faiss_path)
vector_store=FAISS.from_documents(docs,embeddings)
vector_store.save_local(faiss_path)
print("faiss保存完成")





