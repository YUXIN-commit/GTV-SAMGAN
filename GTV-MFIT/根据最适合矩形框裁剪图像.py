import os
from PIL import Image
from tqdm import tqdm  # 引入进度条库

# 初始化裁剪的坐标
crop_min_x, crop_min_y = 48, 13
crop_max_x, crop_max_y = 512, 512

# 创建输出目录如果不存在
output_dir = r"D:\workSpace\cnet\inputs\\CT\\image_256_adaptive"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取图像文件名列表，并初始化进度条
image_files = [filename for filename in os.listdir("D:\workSpace\data\imagesTr2_GT") if filename.endswith(".png")]
pbar = tqdm(image_files)  # 初始化进度条

# 遍历图像目录
for filename in pbar:
    pbar.set_description(f"Processing {filename}")  # 设置进度条描述
    img_path = os.path.join("D:\workSpace\data\imagesTr2_GT", filename)
    
    # 使用PIL读取图像
    img = Image.open(img_path)
    
    # 裁剪图像
    img_cropped = img.crop((crop_min_x, crop_min_y, crop_max_x, crop_max_y))
    
    # 保存裁剪后的图像
    output_path = os.path.join(output_dir, filename)
    img_cropped.save(output_path)

print(f"All images have been cropped and saved in {output_dir}.")
