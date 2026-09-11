"""
Convert and optimize relationship phase photos for horizontal multi-photo sliders.
Preserves EXIF rotation, handles special rotations (e.g. 2025 Ghana match upright),
uses high-density downsampling for retina display clarity, and outputs lightweight WebP images
to assets/images/story/.
"""
import os
from PIL import Image, ImageOps

IMAGES_TO_PROCESS = [
    # Phase 1
    ("Wedding K&S Shoot 1", "our first date in 2015 at golden tulip.jpeg", "story-phase1-01-goldentulip.webp", 0),
    ("Our story imagery", "high school trip to elmina.jpeg", "story-phase1-03-elmina.webp", 0),
    
    # Phase 2
    ("Wedding K&S Shoot 1", "humble beginnings 1.jpeg", "story-phase2-03-humble-beginnings.webp", 0),
    ("Wedding K&S Shoot 1", "2016.jpeg", "story-phase2-04-2016.webp", 0),
    
    # Phase 3
    ("Wedding K&S Shoot 1", "grenada 2.jpeg", "story-phase3-03-grenada.webp", 0),
    
    # Phase 4
    ("Wedding K&S Shoot 1", "reunited in the UK.jpeg", "story-phase4-01-reunited-uk.webp", 0),
    ("Wedding K&S Shoot 1", "the gym in the UK 2020.jpeg", "story-phase4-02-gym.webp", 0),
    ("Wedding K&S Shoot 1", "workout progression.jpeg", "story-phase4-03-workout.webp", 0),
    ("Wedding K&S Shoot 1", "2024 reunited in the UK.jpeg", "story-phase4-04-uk2024.webp", 0),
    
    # Phase 5
    ("Our story imagery", "Shannels 29th this year engaged.jpeg", "story-phase5-01-shannel29.webp", 0),
    ("Wedding K&S Shoot 1", "2025 Ghana match.jpeg", "story-phase5-02-ghanamatch.webp", 90), # Rotated 90 deg counter-clockwise to upright
    ("Wedding K&S Shoot 1", "2025 date in the UK reunited.jpeg", "story-phase5-03-date2025.webp", 0),
]

output_dir = "assets/images/story"
os.makedirs(output_dir, exist_ok=True)

MAX_DIM = 800

print("Optimizing phase slider images...")
for folder, src_name, out_name, extra_rot in IMAGES_TO_PROCESS:
    src_path = os.path.join(folder, src_name)
    out_path = os.path.join(output_dir, out_name)
    
    if not os.path.exists(src_path):
        print(f"ERROR: Source file not found: {src_path}")
        continue
        
    try:
        with Image.open(src_path) as img:
            # Auto-rotate according to EXIF
            img = ImageOps.exif_transpose(img)
            
            # Apply extra rotation if needed
            if extra_rot != 0:
                img = img.rotate(extra_rot, expand=True)
                
            # Convert RGBA/P to RGB if needed
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                
            orig_w, orig_h = img.size
            
            # Calculate target size keeping aspect ratio
            if orig_w > orig_h:
                if orig_w > MAX_DIM:
                    new_w = MAX_DIM
                    new_h = int(orig_h * (MAX_DIM / orig_w))
                else:
                    new_w, new_h = orig_w, orig_h
            else:
                if orig_h > MAX_DIM:
                    new_h = MAX_DIM
                    new_w = int(orig_w * (MAX_DIM / orig_h))
                else:
                    new_w, new_h = orig_w, orig_h
                    
            if (new_w, new_h) != (orig_w, orig_h):
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                
            img.save(out_path, "WEBP", quality=90, method=6)
            size_kb = os.path.getsize(out_path) / 1024
            print(f" Converted: {out_name} ({new_w}x{new_h}, {size_kb:.1f} KB)")
    except Exception as e:
        print(f"Failed to process {src_name}: {e}")

print("All phase slider images optimized successfully.")
