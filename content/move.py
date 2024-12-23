import os
import shutil

def move_files_to_current_directory():
    current_dir = os.getcwd()  # 获取当前工作目录
    
    # 遍历当前目录下的所有子目录
    for subdir in os.listdir(current_dir):
        subdir_path = os.path.join(current_dir, subdir)
        
        # 检查是否是目录
        if os.path.isdir(subdir_path):
            # 遍历子目录中的所有文件
            for file_name in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file_name)
                destination_path = os.path.join(current_dir, file_name)
                
                # 只处理文件
                if os.path.isfile(file_path):
                    # 检查目标文件是否已经存在
                    if os.path.exists(destination_path):
                        print(f"File '{file_name}' already exists in the current directory, skipping.")
                    else:
                        # 将文件移动到当前目录
                        shutil.move(file_path, current_dir)
                        print(f"Moved: {file_name} from {subdir_path} to {current_dir}")
            
            # 可选：如果需要删除空的子目录，可以取消以下行的注释
            # os.rmdir(subdir_path)

# 调用函数
move_files_to_current_directory()
