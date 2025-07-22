import os
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm

# Initialize Variables to Store the Coordinates of the Global Minimum Bounding Rectangle
global_min_x = float('inf')
global_min_y = float('inf')
global_max_x = 0
global_max_y = 0

output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, 'min_rect_coordinates.txt'), 'w') as f:
    image_files = [filename for filename in os.listdir("labelsTr_GT") if filename.endswith(".png")]
    pbar = tqdm(image_files)
    
    for filename in pbar:
        pbar.set_description(f"Processing {filename}")
        img_path = os.path.join("labelsTr_GT", filename)
        
        img = Image.open(img_path).convert('L')
        img = np.array(img)
        
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #Initialize the Coordinates of the Minimum Bounding Rectangle Within the Image
        img_min_x = float('inf')
        img_min_y = float('inf')
        img_max_x = 0
        img_max_y = 0
        
        #Calculate the Minimum Bounding Rectangle Within the Image

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            img_min_x = min(img_min_x, x)
            img_min_y = min(img_min_y, y)
            img_max_x = max(img_max_x, x + w)
            img_max_y = max(img_max_y, y + h)
        
        f.write(f"{filename} 1 {img_min_x} {img_min_y} {img_max_x} {img_max_y}\n")
        
        # Update the Coordinates of the Global Minimum Bounding Rectangle
        global_min_x = min(global_min_x, img_min_x)
        global_min_y = min(global_min_y, img_min_y)
        global_max_x = max(global_max_x, img_max_x)
        global_max_y = max(global_max_y, img_max_y)





image_max_x = 512  # Please Replace with the Actual Maximum Width of Your Image
image_max_y = 512  # Please Replace with the Actual Maximum Height of Your Image
# Output the Coordinates of the Global Minimum Bounding Rectangle, Expanded by 10
expand_value = 10
global_min_x = max(global_min_x - expand_value, 0)
global_min_y = max(global_min_y - expand_value, 0)
global_max_x = min(global_max_x + expand_value, image_max_x)
global_max_y = min(global_max_y + expand_value, image_max_y)


# Calculate the Size of the Current Bounding Rectangle
current_width = global_max_x - global_min_x
current_height = global_max_y - global_min_y

factor = 64  
new_dimension = max(current_width, current_height)
new_dimension = ((new_dimension + factor - 1) // factor) * factor

# Use This New Size as the Length and Width of the Bounding Rectangle
global_max_x = global_min_x + new_dimension
global_max_y = global_min_y + new_dimension

# Ensure These Values Do Not Exceed the Maximum Dimensions of the Image
global_max_x = min(global_max_x, image_max_x)
global_max_y = min(global_max_y, image_max_y)

# Output the Adjusted Coordinates of the Global Minimum Bounding Rectangle
print(f"Adjusted global minimum rectangle coordinates: ({global_min_x}, {global_min_y}) to ({global_max_x}, {global_max_y})")
