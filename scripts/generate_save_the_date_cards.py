import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\save-the-date"
os.makedirs(output_dir, exist_ok=True)
fonts_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\fonts"
images_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\images"

# Colors
GOLD_LIGHT = "#E8C88B"
GOLD_PRIMARY = "#C5A059"
GOLD_DARK = "#8A6926"
ALABASTER = "#FAF8F5"
DARK_OBSIDIAN = "#101010"
CHARCOAL = "#1C1C1C"
WHITE = "#FFFFFF"

cinzel_regular = os.path.join(fonts_dir, "Cinzel-Regular.ttf")
playfair_italic = os.path.join(fonts_dir, "PlayfairDisplay-Italic.ttf")
playfair_regular = os.path.join(fonts_dir, "PlayfairDisplay-Regular.ttf")
jakarta_medium = os.path.join(fonts_dir, "PlusJakartaSans-Medium.ttf")

def draw_centered_text(draw, y, text, font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return y + (bbox[3] - bbox[1])

def draw_spaced_text(draw, y, text, font, fill, width, letter_spacing=6):
    total_w = sum(draw.textbbox((0,0), char, font=font)[2] - draw.textbbox((0,0), char, font=font)[0] + letter_spacing for char in text) - letter_spacing
    x = (width - total_w) // 2
    for char in text:
        draw.text((x, y), char, font=font, fill=fill)
        x += (draw.textbbox((0,0), char, font=font)[2] - draw.textbbox((0,0), char, font=font)[0]) + letter_spacing
    bbox = draw.textbbox((0,0), "A", font=font)
    return y + (bbox[3] - bbox[1])

# ==============================================================================
# CARD 1: EDITORIAL ROYAL GOLD (Story 1080 x 1920)
# ==============================================================================
print("Generating Card 1: Editorial Royal Gold (1080x1920)...")
W, H = 1080, 1920
card1 = Image.new("RGB", (W, H), DARK_OBSIDIAN)
draw1 = ImageDraw.Draw(card1)

# Outer Gold Frame
margin = 44
draw1.rectangle([margin, margin, W - margin, H - margin], outline=GOLD_PRIMARY, width=2)
draw1.rectangle([margin + 8, margin + 8, W - margin - 8, H - margin - 8], outline=GOLD_DARK, width=1)

# Corner Diamonds
for cx, cy in [(margin, margin), (W-margin, margin), (margin, H-margin), (W-margin, H-margin)]:
    d = 8
    draw1.polygon([(cx, cy-d), (cx+d, cy), (cx, cy+d), (cx-d, cy)], fill=GOLD_PRIMARY)

# Monogram Header
f_mono = ImageFont.truetype(cinzel_regular, 36)
draw_spaced_text(draw1, 100, "K  &  S", f_mono, GOLD_PRIMARY, W, 12)

f_eyebrow = ImageFont.truetype(cinzel_regular, 24)
draw_spaced_text(draw1, 160, "SAVE THE DATE", f_eyebrow, GOLD_LIGHT, W, 8)

f_sub = ImageFont.truetype(jakarta_medium, 18)
draw_spaced_text(draw1, 205, "FOR THE WEDDING CELEBRATION OF", f_sub, "#9E9A90", W, 4)

# Couple Names
f_names = ImageFont.truetype(playfair_italic, 88)
draw_centered_text(draw1, 250, "Kevin & Shannel", f_names, WHITE, W)

# Hero Arch Portrait (IMG_0851)
img_path = os.path.join(images_dir, "IMG_0851.webp")
if os.path.exists(img_path):
    src_img = Image.open(img_path).convert("RGBA")
    # Target frame: 680w x 880h
    frame_w, frame_h = 680, 860
    # Crop and scale
    scaled = src_img.resize((frame_w, int(frame_w * src_img.height / src_img.width)), Image.Resampling.LANCZOS)
    cropped = scaled.crop((0, 0, frame_w, frame_h))
    
    # Create Arch Mask
    mask = Image.new("L", (frame_w, frame_h), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rectangle([0, frame_w // 2, frame_w, frame_h], fill=255)
    draw_mask.ellipse([0, 0, frame_w, frame_w], fill=255)
    
    # Frame Position
    fx = (W - frame_w) // 2
    fy = 390
    card1.paste(cropped, (fx, fy), mask)
    
    # Draw Gold Arch Border
    draw1.arc([fx, fy, fx + frame_w, fy + frame_w], start=180, end=0, fill=GOLD_PRIMARY, width=3)
    draw1.line([fx, fy + frame_w // 2, fx, fy + frame_h], fill=GOLD_PRIMARY, width=3)
    draw1.line([fx + frame_w, fy + frame_w // 2, fx + frame_w, fy + frame_h], fill=GOLD_PRIMARY, width=3)
    draw1.line([fx, fy + frame_h, fx + frame_w, fy + frame_h], fill=GOLD_PRIMARY, width=3)

# Date Section
f_date = ImageFont.truetype(cinzel_regular, 34)
draw_spaced_text(draw1, 1310, "SATURDAY", f_date, GOLD_LIGHT, W, 8)

f_date_big = ImageFont.truetype(playfair_regular, 54)
draw_centered_text(draw1, 1365, "9th January 2027", f_date_big, WHITE, W)

# Gold Divider Line
dw = 240
dx = (W - dw) // 2
draw1.line([dx, 1460, dx + dw, 1460], fill=GOLD_PRIMARY, width=1)
draw1.polygon([(W//2, 1456), (W//2+5, 1460), (W//2, 1464), (W//2-5, 1460)], fill=GOLD_PRIMARY)

# Location
f_loc = ImageFont.truetype(cinzel_regular, 26)
draw_spaced_text(draw1, 1490, "LABADI BEACH HOTEL", f_loc, GOLD_LIGHT, W, 6)

f_city = ImageFont.truetype(jakarta_medium, 22)
draw_spaced_text(draw1, 1540, "ACCRA, GHANA", f_city, "#D5D0C5", W, 4)

# Footer Note
f_footer = ImageFont.truetype(jakarta_medium, 19)
draw_spaced_text(draw1, 1680, "FORMAL INVITATION & DETAILS TO FOLLOW", f_footer, "#9E9A90", W, 4)

card1.save(os.path.join(output_dir, "SaveTheDate-1-RoyalGold-Story.png"), quality=95)
print("Saved Card 1!")

# ==============================================================================
# CARD 2: TWILIGHT ROMANCE ARCH (Story 1080 x 1920)
# ==============================================================================
print("Generating Card 2: Twilight Romance Arch (1080x1920)...")
card2 = Image.new("RGB", (W, H), DARK_OBSIDIAN)
img2_path = os.path.join(images_dir, "IMG_0723.webp")
if os.path.exists(img2_path):
    bg_raw = Image.open(img2_path).convert("RGB")
    # Resize to fill
    bg_scaled = bg_raw.resize((W, int(W * bg_raw.height / bg_raw.width)), Image.Resampling.LANCZOS)
    if bg_scaled.height < H:
        bg_scaled = bg_raw.resize((int(H * bg_raw.width / bg_raw.height), H), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (bg_scaled.width - W) // 2
    top = (bg_scaled.height - H) // 2
    card2.paste(bg_scaled.crop((left, top, left + W, top + H)))

# Add Dark Gradient Overlay
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_ov = ImageDraw.Draw(overlay)
for y in range(H):
    # Darker at top and bottom, visible in middle
    if y < 450:
        alpha = int(220 * (1 - y / 450) + 120)
    elif y > 1150:
        alpha = int(235 * ((y - 1150) / (H - 1150)) + 140)
    else:
        alpha = 110
    draw_ov.line([(0, y), (W, y)], fill=(12, 12, 12, alpha))

card2 = Image.alpha_composite(card2.convert("RGBA"), overlay).convert("RGB")
draw2 = ImageDraw.Draw(card2)

# Double Gold Border
draw2.rectangle([48, 48, W - 48, H - 48], outline=GOLD_PRIMARY, width=2)
draw2.rectangle([56, 56, W - 56, H - 56], outline=GOLD_DARK, width=1)

# Top Section
draw_spaced_text(draw2, 130, "SAVE OUR DATE", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W, 8)
draw_centered_text(draw2, 180, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 86), WHITE, W)

# Middle Quote Tag
f_quote = ImageFont.truetype(playfair_italic, 24)
draw_centered_text(draw2, 1050, "“I have found the one whom my soul loves”", f_quote, "#EAE5D9", W)

# Bottom Glass Card Plaque
plaque_h = 420
plaque_w = W - 140
px = 70
py = 1350

plaque = Image.new("RGBA", (plaque_w, plaque_h), (18, 18, 18, 225))
draw_pl = ImageDraw.Draw(plaque)
draw_pl.rectangle([0, 0, plaque_w, plaque_h], outline=GOLD_PRIMARY, width=2)

draw_spaced_text(draw_pl, 45, "THE WHITE WEDDING CELEBRATION", ImageFont.truetype(cinzel_regular, 20), GOLD_LIGHT, plaque_w, 4)
draw_centered_text(draw_pl, 90, "Saturday, 9th January 2027", ImageFont.truetype(playfair_regular, 44), WHITE, plaque_w)

draw_pl.line([(plaque_w//2 - 100, 165), (plaque_w//2 + 100, 165)], fill=GOLD_PRIMARY, width=1)

draw_spaced_text(draw_pl, 195, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, plaque_w, 6)
draw_spaced_text(draw_pl, 240, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 20), WHITE, plaque_w, 4)
draw_spaced_text(draw_pl, 320, "FORMAL INVITATION TO FOLLOW", ImageFont.truetype(jakarta_medium, 16), "#9E9A90", plaque_w, 3)

card2.paste(plaque, (px, py), plaque)
card2.save(os.path.join(output_dir, "SaveTheDate-2-TwilightRomance-Story.png"), quality=95)
print("Saved Card 2!")

# ==============================================================================
# CARD 3: MODERN ALABASTER & GOLD (Square 1080 x 1080)
# ==============================================================================
print("Generating Card 3: Modern Alabaster Square (1080x1080)...")
W3, H3 = 1080, 1080
card3 = Image.new("RGB", (W3, H3), ALABASTER)
draw3 = ImageDraw.Draw(card3)

# Elegant Inset Borders
draw3.rectangle([36, 36, W3 - 36, H3 - 36], outline=GOLD_PRIMARY, width=2)
draw3.rectangle([44, 44, W3 - 44, H3 - 44], outline=GOLD_DARK, width=1)

# Left/Top Circular Photo Frame (IMG_0836)
img3_path = os.path.join(images_dir, "IMG_0836.webp")
if os.path.exists(img3_path):
    raw3 = Image.open(img3_path).convert("RGBA")
    size = 460
    # Center crop square
    w3, h3 = raw3.size
    min_dim = min(w3, h3)
    crop3 = raw3.crop(((w3 - min_dim)//2, (h3 - min_dim)//4, (w3 + min_dim)//2, (h3 - min_dim)//4 + min_dim)).resize((size, size), Image.Resampling.LANCZOS)
    
    # Circular mask
    cmask = Image.new("L", (size, size), 0)
    draw_c = ImageDraw.Draw(cmask)
    draw_c.ellipse([0, 0, size, size], fill=255)
    
    cx, cy = (W3 - size) // 2, 100
    card3.paste(crop3, (cx, cy), cmask)
    
    # Outer gold circle
    draw3.ellipse([cx - 5, cy - 5, cx + size + 5, cy + size + 5], outline=GOLD_PRIMARY, width=3)
    draw3.ellipse([cx - 12, cy - 12, cx + size + 12, cy + size + 12], outline=GOLD_DARK, width=1)

# Typography below circle
draw_spaced_text(draw3, 620, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 22), GOLD_PRIMARY, W3, 8)
draw_centered_text(draw3, 665, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 66), CHARCOAL, W3)

draw3.line([(W3//2 - 120, 765), (W3//2 + 120, 765)], fill=GOLD_PRIMARY, width=1)
draw3.polygon([(W3//2, 762), (W3//2+4, 765), (W3//2, 768), (W3//2-4, 765)], fill=GOLD_PRIMARY)

draw_centered_text(draw3, 790, "Saturday, 9th January 2027", ImageFont.truetype(playfair_regular, 36), CHARCOAL, W3)
draw_spaced_text(draw3, 850, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(cinzel_regular, 20), GOLD_DARK, W3, 4)
draw_spaced_text(draw3, 925, "FORMAL INVITATION TO FOLLOW", ImageFont.truetype(jakarta_medium, 17), "#706E69", W3, 4)

card3.save(os.path.join(output_dir, "SaveTheDate-3-AlabasterGold-Square.png"), quality=95)
print("Saved Card 3!")

# ==============================================================================
# CARD 4: CINEMATIC NOIR POSTCARD (4:5 - 1080 x 1350)
# ==============================================================================
print("Generating Card 4: Cinematic Noir Postcard (1080x1350)...")
W4, H4 = 1080, 1350
card4 = Image.new("RGB", (W4, H4), DARK_OBSIDIAN)
draw4 = ImageDraw.Draw(card4)

# Borders
draw4.rectangle([36, 36, W4 - 36, H4 - 36], outline=GOLD_PRIMARY, width=2)

# Panoramic photo (IMG_0893)
img4_path = os.path.join(images_dir, "IMG_0893.webp")
if os.path.exists(img4_path):
    raw4 = Image.open(img4_path).convert("RGBA")
    # Top banner height 640
    pw, ph = W4 - 96, 640
    scale4 = raw4.resize((pw, int(pw * raw4.height / raw4.width)), Image.Resampling.LANCZOS)
    c4 = scale4.crop((0, (scale4.height - ph)//2, pw, (scale4.height - ph)//2 + ph))
    
    px4, py4 = 48, 48
    card4.paste(c4, (px4, py4))
    draw4.rectangle([px4, py4, px4 + pw, py4 + ph], outline=GOLD_PRIMARY, width=2)

# Text Box in lower portion
draw_spaced_text(draw4, 730, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W4, 8)
draw_spaced_text(draw4, 780, "FOR THE WEDDING OF", ImageFont.truetype(jakarta_medium, 16), "#9E9A90", W4, 4)
draw_centered_text(draw4, 820, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 76), WHITE, W4)

draw4.line([(W4//2 - 140, 930), (W4//2 + 140, 930)], fill=GOLD_PRIMARY, width=1)
draw4.polygon([(W4//2, 926), (W4//2+5, 930), (W4//2, 934), (W4//2-5, 930)], fill=GOLD_PRIMARY)

draw_centered_text(draw4, 960, "Saturday, 9th January 2027", ImageFont.truetype(playfair_regular, 40), WHITE, W4)
draw_spaced_text(draw4, 1025, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W4, 6)
draw_spaced_text(draw4, 1075, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 20), "#D5D0C5", W4, 4)

draw_spaced_text(draw4, 1180, "FORMAL INVITATION & DETAILS TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), "#9E9A90", W4, 4)

card4.save(os.path.join(output_dir, "SaveTheDate-4-CinematicNoir-Postcard.png"), quality=95)
print("Saved Card 4!")

print("\nAll 4 Save the Date cards created successfully in assets/save-the-date/!")
