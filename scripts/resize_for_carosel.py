import os
from PIL import Image

INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
TARGET_HEIGHT = 1080

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def resize_to_height(img, target_height):
    w, h = img.size
    scale = target_height / h
    new_size = (int(w * scale), target_height)
    return img.resize(new_size, Image.Resampling.LANCZOS)

# Step 1: Resize all images and find the max width
resized_images = []
max_width = 0

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        path = os.path.join(INPUT_FOLDER, filename)
        img = Image.open(path).convert("RGBA")
        resized = resize_to_height(img, TARGET_HEIGHT)
        resized_images.append((filename, resized))
        max_width = max(max_width, resized.width)

# Step 2: Pad images to match max width and save
for filename, img in resized_images:
    padded_img = Image.new("RGBA", (max_width, TARGET_HEIGHT), (0, 0, 0, 0))
    x_offset = (max_width - img.width) // 2
    padded_img.paste(img, (x_offset, 0))
    padded_img.save(os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0] + ".png"))

print(f"Processed {len(resized_images)} images. Output saved to '{OUTPUT_FOLDER}'")
