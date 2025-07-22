import os
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm

# Coordinates of the Global Minimum Bounding Rectangle
global_min_x, global_min_y = 48, 13
global_max_x, global_max_y = 512, 512


output_dir = r"test_GT_detection"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_files = [filename for filename in os.listdir("labelsTr_GT") if filename.endswith(".png")]
pbar = tqdm(image_files)

for filename in pbar:
    pbar.set_description(f"Processing {filename}")
    img_path = os.path.join("labelsTr_GT", filename)
    
  
    img = Image.open(img_path).convert('RGB')
    img = np.array(img)
    

    color = (0, 255, 0)  
    thickness = 2
    img = cv2.rectangle(img, (global_min_x, global_min_y), (global_max_x, global_max_y), color, thickness)
    
    # Save the Image with the Drawn Rectangle
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

print(f"All images have been processed and saved in {output_dir}.")
