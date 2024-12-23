ComfyUI:stable diffusion操作界面        
     环境：**comfyui-env**
     大模型共享Webui的
     
Stable-diffusion-webui:stable diffusion操作界面   
     启动：./webui.sh --port 7866
     环境：(**venv**) (**webui-env**) 
     已安装：WD1.4字幕
     
kohya_ss:训练lora     
export HTTP_PROXY="http://127.0.0.1:7897"
export HTTPS_PROXY="http://127.0.0.1:7897"
export SOCKS_PROXY="socks5://127.0.0.1:7897"  
export ALL_PROXY="socks5://127.0.0.1:7897"  
export http_proxy="http://127.0.0.1:7897"
export https_proxy="http://127.0.0.1:7897"
export all_proxy="socks5://127.0.0.1:7897"  
unset HTTP_PROXY HTTPS_PROXY SOCKS_PROXY ALL_PROXY http_proxy https_proxy all_proxy
注意：有时报错ssl1007：刷新代理，不行则 export proxy;
     启动：./gui-cn.sh
     已安装：WD1.4字幕 BLIP字幕
     环境：/venv/bin/activate 同时依赖于python3.10虚拟环境lora-train-env [(**venv**) (**lora-train-env**)]
     使用Multi-LoRA-Composition下载的大模型：model/checkpoint/models--SG161222--Realistic_Vision_V5.1_noVAE/snapshots/672a55008829cf5e581a6a33159daf03c44a0f0b/unet
     TensorBoard注意：
     	1. loss高则说明设置的参数比如：NetworkRank小了
     	2. caption设置(daodanche:1.2)加强触发词
     	3. 适当加入标题丢失率：2个epoch丢失0.03标题丢失率
     日志分析：
       running training / 学習開始
	  num train images * repeats / 学習画像の数×繰り返し回数: 3400=170*20：每张图在一个epoch重复使用20次
	  num reg images / 正則化画像の数: 0
	  num batches per epoch / 1epochのバッチ数: 1700=3400/2：每个epoch处理的总批次数。
	  num epochs / epoch数: 15：完整遍历数据集的次数。
	  batch size per device / バッチサイズ: 2：批量大小。
	  gradient accumulation steps / 勾配を合計するステップ数 = 1：梯度更新次数。
	  total optimization steps / 学習ステップ数: 25000=3400/2*15：总训练步数。
     
dataset-tag-editor-stadalone:
     环境：[(**venv**) (lora-train-env)]
     
图片剪切软件gimp：
     安装：sudo apt-get install gimp
     启动：gimp
     卸载：sudo apt-get remove gimp
Multi-LoRA-Composition:多个LoRA混合
     环境：**multi-lora**
     大模型存在：model文件夹中
     
     
启动Llama：
	ollama run llama2
启动open-webui作为llama的界面：
	conda activate open-webui
	open-webui serve
AnythinLLM启动：
	./home/c303-2/AnythingLLMDesktop/start
	
Docker启动：
sudo systemctl start docker
	

