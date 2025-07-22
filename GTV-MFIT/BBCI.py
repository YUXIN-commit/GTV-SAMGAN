import os
from PIL import Image
from tqdm import tqdm  

#Initialize the Cropping Coordinates
crop_min_x, crop_min_y = 48, 13
crop_max_x, crop_max_y = 512, 512


output_dir = r"image_256_adaptive"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


image_files = [filename for filename in os.listdir("imagesTr_GT") if filename.endswith(".png")]
pbar = tqdm(image_files)  

# Iterate Through the Image Directory
for filename in pbar:
    pbar.set_description(f"Processing {filename}")  
    img_path = os.path.join("imagesTr2_GT", filename)
    

    img = Image.open(img_path)
    

    img_cropped = img.crop((crop_min_x, crop_min_y, crop_max_x, crop_max_y))
    
    output_path = os.path.join(output_dir, filename)
    img_cropped.save(output_path)

print(f"All images have been cropped and saved in {output_dir}.")
