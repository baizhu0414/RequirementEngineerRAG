from transformers import AutoTokenizer, AutoModelForCausalLM


# 加载tokenizer
tokenizer = AutoTokenizer.from_pretrained('TheBloke/Llama-2-7B-Chat-GPTQ')
# 加载本地基础模型
base_model = AutoModelForCausalLM.from_pretrained(
        "TheBloke/Llama-2-7B-Chat-GPTQ",
        trust_remote_code=True,
    ).to('cuda')
model=base_model.eval()

while True:
    # test_query_str = "different aspects of security and access control, prevent, delete, validate"
    test_query_str = input("请输入问题: ")

    if test_query_str == "exit":
        print("程序已退出")
        break

    
    # 把prompt输入模型进行预测
    inputs = tokenizer([f"Question: {test_query_str} \nLLM Answer:\n"], return_tensors="pt")
    # 输入文本的 token id 列表（张量格式）
    input_ids = inputs["input_ids"].to('cuda')

    generate_input = {
        "input_ids":input_ids,
        "max_new_tokens":2048, # 限制生成的最大长度。
        "do_sample":True, # 决定是否使用随机性生成。
        "top_k":50, # 限制生成时考虑的最可能的k个token。
        "top_p":0.95, # 控制生成时核采样的累积概率阈值。
        "temperature":0.3, # 调整生成文本的多样性
        "repetition_penalty":1.3 # 减少生成重复内容的倾向。
    }
    generate_ids  = model.generate(**generate_input)

    # 将模型生成的 token 序列（generate_ids[0]）解码为可读的文本，并且跳过任何特殊的 token
    new_tokens = tokenizer.decode(generate_ids[0], skip_special_tokens=True) 
    print("new_tokens:\n"+new_tokens)
