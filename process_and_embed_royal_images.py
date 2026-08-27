# -*- coding: utf-8 -*-
import os, sys, shutil
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
royal_src_dir = os.path.join(base_dir, "صور العائلة الملكية")

v2_img_dir = os.path.join(base_dir, "التقرير_الاحترافي_المطور", "assets", "images")
v1_img_dir = os.path.join(base_dir, "التقرير_الجديد", "assets", "images")

os.makedirs(v2_img_dir, exist_ok=True)
os.makedirs(v1_img_dir, exist_ok=True)

# 1. Process and save images
img_mapping = {
    "الملك سلمان بن عبدالعزيز.jpg": "king_salman.jpg",
    "محمد بن سلمان.jpg": "crown_prince.jpg",
    "سلمان بن سلطان.jfif": "prince_salman.jpg"
}

for src_name, target_name in img_mapping.items():
    src_path = os.path.join(royal_src_dir, src_name)
    if os.path.exists(src_path):
        img = Image.open(src_path).convert("RGB")
        target_path_v2 = os.path.join(v2_img_dir, target_name)
        target_path_v1 = os.path.join(v1_img_dir, target_name)
        img.save(target_path_v2, "JPEG", quality=95)
        img.save(target_path_v1, "JPEG", quality=95)
        print(f"Processed and copied: {target_name}")

print("Royal images processed successfully.")
