# 一、手动编写RAG环境介绍
## 1.1、root权限
`sudo -i`:   
- 切换到root权限运行

## 1.2、配置环境
```shell
conda env create -f environment.yml
```
[environment.yml](./environment.yml)

## 1.3、结构

1. `knowledge_emb.py`  
- 学习知识嵌入  
2. `rag.py`  
- 加载模型
- 推理过程
3. `no-rag.py`
- 不适用rag的推理过程，用于对比分析

# 二、使用AnyLLM封装程序环境介绍
## 2.1、配置环境
```shell
https://github.com/Mintplex-Labs/anything-llm
```
## 2.2、启动
参考[readme-env.txt](./readme-env.txt)

## 2.3、分析结果
参考[score.txt](./AnyLLMScore/score.txt)