import os
from PIL import Image, ImageOps

source_dir = r"Our story imagery"
target_dir = r"assets/images/story"
os.makedirs(target_dir, exist_ok=True)

image_mapping = [
    ("us in highschool where we met.jpeg", "story-01-highschool-meet.webp", 760),
    ("highschool trip to the beach.jpeg", "story-02-beach-trip.webp", 800),
    ("my 18th bday party held at labadi beach hotel.jpeg", "story-03-labadi-18th-bday.webp", 760),
    ("high school leavers dinner smiles.jpeg", "story-04-leavers-dinner.webp", 760),
    ("Shannel visits me in sheffield.jpg", "story-05-sheffield-visit.webp", 800),
    ("trip to visit shannel in grenada 2018.jpeg", "story-06-grenada-trip.webp", 800),
    ("A date in Ghana reunited on break from uni.jpg", "story-07-ghana-reunited.webp", 760),
    ("20171228_150127.jpg", "story-08-bicycle-date.webp", 760),
]

print("Starting Story Images Optimization Pipeline...")

for src_name, tgt_name, max_dim in image_mapping:
    src_path = os.path.join(source_dir, src_name)
    tgt_path = os.path.join(target_dir, tgt_name)
    
    if not os.path.exists(src_path):
        print(f"Warning: Source not found: {src_path}")
        continue
        
    with Image.open(src_path) as img:
        # Correct orientation based on EXIF
        img = ImageOps.exif_transpose(img)
        
        # Convert to RGB if needed
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        w, h = img.size
        # Resize while maintaining aspect ratio, capping max dimension
        if max(w, h) > max_dim:
            if w > h:
                new_w = max_dim
                new_h = int(h * (max_dim / w))
            else:
                new_h = max_dim
                new_w = int(w * (max_dim / h))
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
        # Save as optimized WebP
        img.save(tgt_path, "WEBP", quality=90, method=6)
        file_size_kb = os.path.getsize(tgt_path) / 1024
        print(f"Optimized: {tgt_name} | {img.size[0]}x{img.size[1]} | {file_size_kb:.1f} KB")

print("\nOptimization complete! All story assets ready in assets/images/story/")
