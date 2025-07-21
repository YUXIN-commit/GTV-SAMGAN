import cv2
import os
import glob
import numpy as np
from tqdm import tqdm

# 原图像的尺寸
original_size = (512, 512)

# 裁剪区域的坐标
global_min_x, global_min_y = 0, 0
global_max_x, global_max_y = 256, 256

# 输入和输出文件夹路径
input_folder = r'D:\workSpace\cnet\save_Unet_CT_Baseline_SE'
output_folder = r'D:\workSpace\cnet\save_Unet_CT_Baseline_SE_512'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取所有图像路径
image_paths = glob.glob(os.path.join(input_folder, '*.png'))

# 遍历输入文件夹中的所有图像
for img_path in tqdm(image_paths, desc="Processing images"):
    # 读取图像
    img = cv2.imread(img_path)

    # 创建一个空的原始尺寸图像
    restored_img = np.zeros((original_size[1], original_size[0], 3), dtype=np.uint8)

    # 将裁剪后的图像放置在正确的位置
    restored_img[global_min_y:global_max_y, global_min_x:global_max_x] = img

    # 保存还原后的图像
    output_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(output_path, restored_img)
