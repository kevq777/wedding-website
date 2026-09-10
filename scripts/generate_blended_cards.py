import os
import math
from PIL import Image, ImageDraw, ImageFont

output_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\save-the-date"
os.makedirs(output_dir, exist_ok=True)
fonts_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\fonts"
images_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\images"

# Typography Fonts
cinzel_regular = os.path.join(fonts_dir, "Cinzel-Regular.ttf")
playfair_italic = os.path.join(fonts_dir, "PlayfairDisplay-Italic.ttf")
playfair_regular = os.path.join(fonts_dir, "PlayfairDisplay-Regular.ttf")
jakarta_medium = os.path.join(fonts_dir, "PlusJakartaSans-Medium.ttf")

GOLD_LIGHT = "#E8C88B"
GOLD_PRIMARY = "#C5A059"
WHITE = "#FFFFFF"
CREAM = "#F5F2EC"
SUBTLE_GREY = "#9C978D"

def create_smooth_fade_mask(width, height, fade_start, fade_end):
    fade_len = max(1, fade_end - fade_start)
    col_bytes = bytearray()
    for y in range(height):
        if y < fade_start:
            val = 255
        elif y >= fade_end:
            val = 0
        else:
            t = (y - fade_start) / fade_len
            val = int(255 * (0.5 + 0.5 * math.cos(math.pi * t)))
        col_bytes.append(val)
    col_img = Image.frombytes("L", (1, height), bytes(col_bytes))
    return col_img.resize((width, height), Image.Resampling.NEAREST)

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
# CARD 1: PHOTO 0844 — The Ring Gaze (Warm Noir Seamless Blend)
# ==============================================================================
print("Rendering Card 1 with IMG_0844 (Seamless Fade)...")
W, H = 1080, 1920
BG_0844 = (14, 14, 15)
card1 = Image.new("RGB", (W, H), BG_0844)

img1_raw = Image.open(os.path.join(images_dir, "IMG_0844.webp")).convert("RGBA")
# Scale photo to height 1080 so that faces and hands are prominent and well within frame
target_h1 = 1050
target_w1 = int(target_h1 * img1_raw.width / img1_raw.height)
img1_scaled = img1_raw.resize((target_w1, target_h1), Image.Resampling.LANCZOS)

# Center crop horizontally to 1080
left_crop1 = (target_w1 - W) // 2
img1_cropped = img1_scaled.crop((left_crop1, 0, left_crop1 + W, target_h1))

# Fade between y=650 and y=1020 (well before target_h1=1050)
mask1 = create_smooth_fade_mask(W, target_h1, 620, 1020)
card1.paste(img1_cropped, (0, 0), mask1)

# Top Vignette
top_ov1 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t1 = ImageDraw.Draw(top_ov1)
for y in range(260):
    alpha = int(140 * (1 - y/260))
    draw_t1.line([(0, y), (W, y)], fill=(14, 14, 15, alpha))
card1.paste(top_ov1, (0, 0), top_ov1)

draw1 = ImageDraw.Draw(card1)
draw_spaced_text(draw1, 60, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W, 8)

# Seamless Typography emerging from the fade
draw_spaced_text(draw1, 1070, "THE WEDDING CELEBRATION OF", ImageFont.truetype(cinzel_regular, 20), GOLD_LIGHT, W, 6)
draw_centered_text(draw1, 1120, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W)

# Gold Divider Diamond
dw = 220
dx = (W - dw) // 2
draw1.line([dx, 1265, dx + dw, 1265], fill=GOLD_PRIMARY, width=1)
draw1.polygon([(W//2, 1261), (W//2+5, 1265), (W//2, 1269), (W//2-5, 1265)], fill=GOLD_PRIMARY)

draw_spaced_text(draw1, 1310, "SATURDAY", ImageFont.truetype(cinzel_regular, 32), GOLD_LIGHT, W, 8)
draw_centered_text(draw1, 1365, "9th January 2027", ImageFont.truetype(playfair_regular, 54), CREAM, W)

draw_spaced_text(draw1, 1480, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W, 6)
draw_spaced_text(draw1, 1530, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W, 4)

draw_spaced_text(draw1, 1720, "FORMAL INVITATION & DETAILS TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card1.save(os.path.join(output_dir, "SaveTheDate-0844-RingGaze-Story.png"), quality=96)
print("Saved SaveTheDate-0844-RingGaze-Story.png!")

# ==============================================================================
# CARD 2: PHOTO 0704 — Rooftop Twilight Gaze (Midnight Blue Fade)
# ==============================================================================
print("Rendering Card 2 with IMG_0704 (Seamless Fade)...")
BG_0704 = (10, 12, 18)
card2 = Image.new("RGB", (W, H), BG_0704)

img2_raw = Image.open(os.path.join(images_dir, "IMG_0704.webp")).convert("RGBA")
pw2 = W
ph2 = int(pw2 * img2_raw.height / img2_raw.width)
img2_scaled = img2_raw.resize((pw2, ph2), Image.Resampling.LANCZOS)

fade_start2 = 820
fade_end2 = 1200
mask2 = create_smooth_fade_mask(pw2, ph2, fade_start2, fade_end2)
card2.paste(img2_scaled, (0, 0), mask2)

# Top Soft Vignette
top_ov2 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t2 = ImageDraw.Draw(top_ov2)
for y in range(260):
    alpha = int(120 * (1 - y/260))
    draw_t2.line([(0, y), (W, y)], fill=(10, 12, 18, alpha))
card2.paste(top_ov2, (0, 0), top_ov2)

draw2 = ImageDraw.Draw(card2)
draw_spaced_text(draw2, 60, "SAVE OUR DATE", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W, 8)

draw_centered_text(draw2, 1150, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 96), WHITE, W)
draw_centered_text(draw2, 1270, "“I have found the one whom my soul loves”", ImageFont.truetype(playfair_italic, 26), GOLD_LIGHT, W)

draw2.line([(W//2 - 180, 1340), (W//2 + 180, 1340)], fill=GOLD_PRIMARY, width=1)

draw_spaced_text(draw2, 1380, "SATURDAY, 9TH JANUARY 2027", ImageFont.truetype(cinzel_regular, 30), WHITE, W, 6)
draw_spaced_text(draw2, 1445, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W, 5)
draw_spaced_text(draw2, 1500, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), CREAM, W, 4)

draw_spaced_text(draw2, 1720, "FORMAL INVITATION TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card2.save(os.path.join(output_dir, "SaveTheDate-0704-TwilightEmbrace-Story.png"), quality=96)
print("Saved SaveTheDate-0704-TwilightEmbrace-Story.png!")

# ==============================================================================
# CARD 3: PHOTO 0855 — Tropical Palm Smiles (Tropical Olive / Dark Fade)
# ==============================================================================
print("Rendering Card 3 with IMG_0855 (Seamless Fade)...")
BG_0855 = (14, 18, 16)
card3 = Image.new("RGB", (W, H), BG_0855)

img3_raw = Image.open(os.path.join(images_dir, "IMG_0855.webp")).convert("RGBA")
pw3 = W
ph3 = int(pw3 * img3_raw.height / img3_raw.width)
img3_scaled = img3_raw.resize((pw3, ph3), Image.Resampling.LANCZOS)

fade_start3 = 780
fade_end3 = 1180
mask3 = create_smooth_fade_mask(pw3, ph3, fade_start3, fade_end3)
card3.paste(img3_scaled, (0, 0), mask3)

top_ov3 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t3 = ImageDraw.Draw(top_ov3)
for y in range(260):
    alpha = int(130 * (1 - y/260))
    draw_t3.line([(0, y), (W, y)], fill=(14, 18, 16, alpha))
card3.paste(top_ov3, (0, 0), top_ov3)

draw3 = ImageDraw.Draw(card3)
draw_spaced_text(draw3, 60, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W, 8)

draw_spaced_text(draw3, 1130, "PLEASE JOIN US TO CELEBRATE", ImageFont.truetype(cinzel_regular, 20), GOLD_LIGHT, W, 5)
draw_centered_text(draw3, 1175, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W)

draw3.line([(W//2 - 160, 1310), (W//2 + 160, 1310)], fill=GOLD_PRIMARY, width=1)
draw3.polygon([(W//2, 1306), (W//2+5, 1310), (W//2, 1314), (W//2-5, 1310)], fill=GOLD_PRIMARY)

draw_centered_text(draw3, 1350, "Saturday, 9th January 2027", ImageFont.truetype(playfair_regular, 50), CREAM, W)
draw_spaced_text(draw3, 1435, "TROPICAL GARDEN GLAMOUR", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W, 6)
draw_spaced_text(draw3, 1485, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W, 4)

draw_spaced_text(draw3, 1720, "FORMAL INVITATION & DETAILS TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card3.save(os.path.join(output_dir, "SaveTheDate-0855-TropicalJoy-Story.png"), quality=96)
print("Saved SaveTheDate-0855-TropicalJoy-Story.png!")

# ==============================================================================
# CARD 4: PHOTO 0864 — Appleyard Roses & Diamond Ring (Velvet Crimson Fade)
# ==============================================================================
print("Rendering Card 4 with IMG_0864 (Seamless Fade)...")
BG_0864 = (14, 11, 12)
card4 = Image.new("RGB", (W, H), BG_0864)

img4_raw = Image.open(os.path.join(images_dir, "IMG_0864.webp")).convert("RGBA")
pw4 = W
ph4 = int(pw4 * img4_raw.height / img4_raw.width)
img4_scaled = img4_raw.resize((pw4, ph4), Image.Resampling.LANCZOS)

fade_start4 = 760
fade_end4 = 1150
mask4 = create_smooth_fade_mask(pw4, ph4, fade_start4, fade_end4)
card4.paste(img4_scaled, (0, 0), mask4)

top_ov4 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t4 = ImageDraw.Draw(top_ov4)
for y in range(260):
    alpha = int(140 * (1 - y/260))
    draw_t4.line([(0, y), (W, y)], fill=(14, 11, 12, alpha))
card4.paste(top_ov4, (0, 0), top_ov4)

draw4 = ImageDraw.Draw(card4)
draw_spaced_text(draw4, 60, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W, 8)

draw_spaced_text(draw4, 1120, "A PROMISE FOR FOREVER", ImageFont.truetype(cinzel_regular, 20), GOLD_LIGHT, W, 6)
draw_centered_text(draw4, 1170, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W)

draw4.line([(W//2 - 160, 1300), (W//2 + 160, 1300)], fill=GOLD_PRIMARY, width=1)
draw4.polygon([(W//2, 1296), (W//2+5, 1300), (W//2, 1304), (W//2-5, 1300)], fill=GOLD_PRIMARY)

draw_spaced_text(draw4, 1340, "SATURDAY", ImageFont.truetype(cinzel_regular, 30), GOLD_LIGHT, W, 8)
draw_centered_text(draw4, 1395, "9th January 2027", ImageFont.truetype(playfair_regular, 52), CREAM, W)

draw_spaced_text(draw4, 1495, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W, 6)
draw_spaced_text(draw4, 1545, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W, 4)

draw_spaced_text(draw4, 1720, "FORMAL INVITATION TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card4.save(os.path.join(output_dir, "SaveTheDate-0864-RoseDiamond-Story.png"), quality=96)
print("Saved SaveTheDate-0864-RoseDiamond-Story.png!")

print("\nAll 4 seamless gradient blend cards re-rendered successfully!")
