import cv2
import os
import glob
import numpy as np
from tqdm import tqdm

# Original Image Size
original_size = (512, 512)

#Coordinates of the Cropping Region
global_min_x, global_min_y = 0, 0
global_max_x, global_max_y = 256, 256

input_folder = r'save_256'
output_folder = r'save_512'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_paths = glob.glob(os.path.join(input_folder, '*.png'))

for img_path in tqdm(image_paths, desc="Processing images"):

    img = cv2.imread(img_path)

    restored_img = np.zeros((original_size[1], original_size[0], 3), dtype=np.uint8)

    restored_img[global_min_y:global_max_y, global_min_x:global_max_x] = img

    output_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(output_path, restored_img)
