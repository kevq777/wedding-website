import os
import math
from PIL import Image, ImageDraw, ImageFont

output_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\save-the-date"
os.makedirs(output_dir, exist_ok=True)
fonts_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\fonts"
images_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\images"

cinzel_regular = os.path.join(fonts_dir, "Cinzel-Regular.ttf")
playfair_italic = os.path.join(fonts_dir, "PlayfairDisplay-Italic.ttf")
playfair_regular = os.path.join(fonts_dir, "PlayfairDisplay-Regular.ttf")
jakarta_medium = os.path.join(fonts_dir, "PlusJakartaSans-Medium.ttf")

GOLD_LIGHT = "#E8C88B"
GOLD_PRIMARY = "#C5A059"
WHITE = "#FFFFFF"
CREAM = "#F5F2EC"
SUBTLE_GREY = "#9C978D"

W, H = 1080, 1920

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
# REDO CARD 1: PHOTO 0851 — Formal Black Tie (Seamless Gradient Fade)
# ==============================================================================
print("Rendering Faded Card 1 with IMG_0851...")
BG_0851 = (14, 14, 15)
card1 = Image.new("RGB", (W, H), BG_0851)

img1_raw = Image.open(os.path.join(images_dir, "IMG_0851.webp")).convert("RGBA")
pw1 = W
ph1 = int(pw1 * img1_raw.height / img1_raw.width)
img1_scaled = img1_raw.resize((pw1, ph1), Image.Resampling.LANCZOS)

# Smooth bottom fade between y=760 and y=1160
fade_start1 = 760
fade_end1 = 1160
mask1 = create_smooth_fade_mask(pw1, ph1, fade_start1, fade_end1)
card1.paste(img1_scaled, (0, 0), mask1)

# Subtle Top Vignette for eyebrow legibility
top_ov1 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t1 = ImageDraw.Draw(top_ov1)
for y in range(260):
    alpha = int(140 * (1 - y/260))
    draw_t1.line([(0, y), (W, y)], fill=(14, 14, 15, alpha))
card1.paste(top_ov1, (0, 0), top_ov1)

draw1 = ImageDraw.Draw(card1)
draw_spaced_text(draw1, 60, "SAVE THE DATE", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W, 8)

# Seamless Typography emerging from the fade
draw_spaced_text(draw1, 1100, "THE WEDDING CELEBRATION OF", ImageFont.truetype(cinzel_regular, 20), GOLD_LIGHT, W, 6)
draw_centered_text(draw1, 1150, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W)

# Gold Divider Diamond
dw = 220
dx = (W - dw) // 2
draw1.line([dx, 1290, dx + dw, 1290], fill=GOLD_PRIMARY, width=1)
draw1.polygon([(W//2, 1286), (W//2+5, 1290), (W//2, 1294), (W//2-5, 1290)], fill=GOLD_PRIMARY)

draw_spaced_text(draw1, 1335, "SATURDAY", ImageFont.truetype(cinzel_regular, 32), GOLD_LIGHT, W, 8)
draw_centered_text(draw1, 1390, "9th January 2027", ImageFont.truetype(playfair_regular, 54), CREAM, W)

draw_spaced_text(draw1, 1495, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W, 6)
draw_spaced_text(draw1, 1545, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W, 4)

draw_spaced_text(draw1, 1720, "FORMAL INVITATION & DETAILS TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card1.save(os.path.join(output_dir, "SaveTheDate-1-RoyalGold-Story.png"), quality=96)
card1.save(os.path.join(output_dir, "SaveTheDate-0851-FormalBlackTie-Story.png"), quality=96)
print("Saved Faded Card 1 (IMG_0851)!")

# ==============================================================================
# REDO CARD 2: PHOTO 0723 — Twilight Rooftop Candlelight (Seamless Gradient Fade)
# ==============================================================================
print("Rendering Faded Card 2 with IMG_0723...")
BG_0723 = (11, 12, 16) # Deep twilight midnight tone
card2 = Image.new("RGB", (W, H), BG_0723)

img2_raw = Image.open(os.path.join(images_dir, "IMG_0723.webp")).convert("RGBA")
pw2 = W
ph2 = int(pw2 * img2_raw.height / img2_raw.width)
img2_scaled = img2_raw.resize((pw2, ph2), Image.Resampling.LANCZOS)

# Smooth bottom fade between y=780 and y=1180
fade_start2 = 780
fade_end2 = 1180
mask2 = create_smooth_fade_mask(pw2, ph2, fade_start2, fade_end2)
card2.paste(img2_scaled, (0, 0), mask2)

# Subtle Top Vignette
top_ov2 = Image.new("RGBA", (W, 260), (0,0,0,0))
draw_t2 = ImageDraw.Draw(top_ov2)
for y in range(260):
    alpha = int(130 * (1 - y/260))
    draw_t2.line([(0, y), (W, y)], fill=(11, 12, 16, alpha))
card2.paste(top_ov2, (0, 0), top_ov2)

draw2 = ImageDraw.Draw(card2)
draw_spaced_text(draw2, 60, "SAVE OUR DATE", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W, 8)

# Seamless Typography emerging from the fade
draw_centered_text(draw2, 1140, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W)
draw_centered_text(draw2, 1260, "“I have found the one whom my soul loves”", ImageFont.truetype(playfair_italic, 26), GOLD_LIGHT, W)

draw2.line([(W//2 - 180, 1330), (W//2 + 180, 1330)], fill=GOLD_PRIMARY, width=1)

draw_spaced_text(draw2, 1370, "SATURDAY, 9TH JANUARY 2027", ImageFont.truetype(cinzel_regular, 30), WHITE, W, 6)
draw_spaced_text(draw2, 1435, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W, 5)
draw_spaced_text(draw2, 1490, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), CREAM, W, 4)

draw_spaced_text(draw2, 1720, "FORMAL INVITATION & DETAILS TO FOLLOW", ImageFont.truetype(jakarta_medium, 18), SUBTLE_GREY, W, 4)

card2.save(os.path.join(output_dir, "SaveTheDate-2-TwilightRomance-Story.png"), quality=96)
card2.save(os.path.join(output_dir, "SaveTheDate-0723-TwilightCandlelight-Story.png"), quality=96)
print("Saved Faded Card 2 (IMG_0723)!")

print("\nBoth Card 1 and Card 2 successfully re-rendered in seamless faded format!")
