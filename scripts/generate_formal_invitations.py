import os
import math
from PIL import Image, ImageDraw, ImageFont

output_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\invitations"
os.makedirs(output_dir, exist_ok=True)
fonts_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\fonts"
images_dir = r"c:\Users\kevqu\OneDrive\Documents\VSCode Repos\Wedding Website\assets\images"

# Typography Fonts
cinzel_regular = os.path.join(fonts_dir, "Cinzel-Regular.ttf")
playfair_italic = os.path.join(fonts_dir, "PlayfairDisplay-Italic.ttf")
playfair_regular = os.path.join(fonts_dir, "PlayfairDisplay-Regular.ttf")
jakarta_medium = os.path.join(fonts_dir, "PlusJakartaSans-Medium.ttf")

# Master Color Tokens
GOLD_PRIMARY = "#C5A059"
GOLD_LIGHT = "#E8C88B"
GOLD_DEEP = "#A38038"
CHARCOAL = "#1C1B1A"
CHARCOAL_MUTED = "#544F46"
WHITE = "#FFFFFF"
ALABASTER = "#FAF7F2"
IVORY_BORDER = "#E8E2D5"
EMERALD_NOIR = "#0B1712"

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

def draw_gold_divider(draw, y, width, line_width=240, color=GOLD_PRIMARY):
    dx = (width - line_width) // 2
    draw.line([dx, y, dx + line_width, y], fill=color, width=1)
    # Center diamond
    cx = width // 2
    draw.polygon([(cx, y-5), (cx+5, y), (cx, y+5), (cx-5, y)], fill=color)

def draw_ornate_corners(draw, x0, y0, x1, y1, size=24, color=GOLD_PRIMARY):
    # Top Left
    draw.line([x0, y0 + size, x0, y0, x0 + size, y0], fill=color, width=2)
    # Top Right
    draw.line([x1 - size, y0, x1, y0, x1, y0 + size], fill=color, width=2)
    # Bottom Left
    draw.line([x0, y1 - size, x0, y1, x0 + size, y1], fill=color, width=2)
    # Bottom Right
    draw.line([x1 - size, y1, x1, y1, x1, y1 - size], fill=color, width=2)


# ==============================================================================
# CARD 1: "THE ROYAL ALABASTER" (Clean Ivory, Gold Embossed Crest, Arched Photo)
# 1080 x 1920 (Portrait 9:16)
# ==============================================================================
print("1/4 Generating Card 1: The Royal Alabaster (1080x1920)...")
W1, H1 = 1080, 1920
card1 = Image.new("RGB", (W1, H1), ALABASTER)
draw1 = ImageDraw.Draw(card1)

# Outer and Inner Luxury Double Gold Border
draw1.rectangle([36, 36, W1 - 36, H1 - 36], outline=GOLD_PRIMARY, width=2)
draw1.rectangle([46, 46, W1 - 46, H1 - 46], outline=IVORY_BORDER, width=1)
draw_ornate_corners(draw1, 56, 56, W1 - 56, H1 - 56, size=28, color=GOLD_PRIMARY)

# Gold Crest at Top
crest_raw = Image.open(os.path.join(images_dir, "ks-crest-gold.png")).convert("RGBA")
crest_w1 = 150
crest_h1 = int(crest_raw.height * (crest_w1 / crest_raw.width))
crest_scaled = crest_raw.resize((crest_w1, crest_h1), Image.Resampling.LANCZOS)
card1.paste(crest_scaled, ((W1 - crest_w1) // 2, 75), crest_scaled)

# Formal Invitation Opening
draw_spaced_text(draw1, 310, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 20), "#7D7565", W1, 6)
draw_centered_text(draw1, 350, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 88), CHARCOAL, W1)
draw_spaced_text(draw1, 465, "REQUEST THE HONOUR OF YOUR PRESENCE AT", ImageFont.truetype(cinzel_regular, 18), "#7D7565", W1, 4)
draw_spaced_text(draw1, 500, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 28), GOLD_DEEP, W1, 7)

# Arched Frame Photo in Center: Seated Queen, Standing King
photo1_raw = Image.open(os.path.join(images_dir, "seated-queen-standing-king.webp")).convert("RGBA")
fw, fh = 780, 680
fx = (W1 - fw) // 2
fy = 570

# Create Arched Mask
arch_mask = Image.new("L", (fw, fh), 0)
draw_am = ImageDraw.Draw(arch_mask)
# Top semicircle arch: radius = fw // 2
r = fw // 2
draw_am.pieslice([0, 0, fw, fw], 180, 360, fill=255)
draw_am.rectangle([0, r, fw, fh], fill=255)

# Scale and center-crop photo to (fw, fh)
scale1 = max(fw / photo1_raw.width, fh / photo1_raw.height)
pw1 = int(photo1_raw.width * scale1)
ph1 = int(photo1_raw.height * scale1)
photo1_scaled = photo1_raw.resize((pw1, ph1), Image.Resampling.LANCZOS)
cx1 = (pw1 - fw) // 2
cy1 = int((ph1 - fh) * 0.15)
photo1_cropped = photo1_scaled.crop((cx1, cy1, cx1 + fw, cy1 + fh))

# Paste with arch mask
card1.paste(photo1_cropped, (fx, fy), arch_mask)

# Draw Delicate Gold Arch Border over photo
arch_border = Image.new("RGBA", (fw, fh), (0,0,0,0))
draw_ab = ImageDraw.Draw(arch_border)
draw_ab.arc([1, 1, fw - 2, fw - 2], 180, 360, fill=GOLD_PRIMARY, width=2)
draw_ab.line([1, r, 1, fh - 1], fill=GOLD_PRIMARY, width=2)
draw_ab.line([fw - 2, r, fw - 2, fh - 1], fill=GOLD_PRIMARY, width=2)
draw_ab.line([1, fh - 1, fw - 1, fh - 1], fill=GOLD_PRIMARY, width=2)
card1.paste(arch_border, (fx, fy), arch_border)

# Formal Event Details & Venue
draw_gold_divider(draw1, 1305, W1, 260, GOLD_PRIMARY)

draw_spaced_text(draw1, 1350, "SATURDAY", ImageFont.truetype(cinzel_regular, 24), GOLD_PRIMARY, W1, 8)
draw_centered_text(draw1, 1395, "9th January 2027", ImageFont.truetype(playfair_regular, 62), CHARCOAL, W1)
draw_spaced_text(draw1, 1485, "CEREMONY AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 18), CHARCOAL_MUTED, W1, 4)

draw_spaced_text(draw1, 1550, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 32), GOLD_DEEP, W1, 6)
draw_spaced_text(draw1, 1600, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), CHARCOAL, W1, 5)

draw_spaced_text(draw1, 1665, "RECEPTION & DINNER TO FOLLOW", ImageFont.truetype(cinzel_regular, 19), CHARCOAL_MUTED, W1, 4)

# RSVP and Website
draw1.line([(W1 - 180) // 2, 1720, (W1 + 180) // 2, 1720], fill=IVORY_BORDER, width=1)
draw_spaced_text(draw1, 1750, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 18), GOLD_DEEP, W1, 3)
draw_spaced_text(draw1, 1795, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 20), CHARCOAL, W1, 5)

card1.save(os.path.join(output_dir, "Invitation-1-RoyalAlabaster-Story.png"), quality=95)
print("Saved Card 1.")


# ==============================================================================
# CARD 2: "THE ENCHANTED EMERALD" (Deep Forest Noir, Warm Candlelight Fade)
# 1080 x 1920 (Portrait 9:16)
# ==============================================================================
print("2/4 Generating Card 2: The Enchanted Emerald (1080x1920)...")
W2, H2 = 1080, 1920
card2 = Image.new("RGB", (W2, H2), (11, 23, 18)) # Deep Emerald Noir

img2_raw = Image.open(os.path.join(images_dir, "IMG_0851.webp")).convert("RGBA")
target_h2 = 1060
target_w2 = int(target_h2 * img2_raw.width / img2_raw.height)
img2_scaled = img2_raw.resize((target_w2, target_h2), Image.Resampling.LANCZOS)
left_crop2 = (target_w2 - W2) // 2
img2_cropped = img2_scaled.crop((left_crop2, 0, left_crop2 + W2, target_h2))

mask2 = create_smooth_fade_mask(W2, target_h2, 600, 1040)
card2.paste(img2_cropped, (0, 0), mask2)

# Emerald/Noir Top Vignette
top_ov2 = Image.new("RGBA", (W2, 280), (0,0,0,0))
draw_t2 = ImageDraw.Draw(top_ov2)
for y in range(280):
    alpha = int(160 * (1 - y/280))
    draw_t2.line([(0, y), (W2, y)], fill=(11, 23, 18, alpha))
card2.paste(top_ov2, (0, 0), top_ov2)

draw2 = ImageDraw.Draw(card2)

# Outer Gold Fillet
draw2.rectangle([34, 34, W2 - 34, H2 - 34], outline=GOLD_PRIMARY, width=1)
draw_ornate_corners(draw2, 44, 44, W2 - 44, H2 - 44, size=24, color=GOLD_LIGHT)

# Header
draw_spaced_text(draw2, 65, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W2, 8)
draw_spaced_text(draw2, 105, "FORMAL INVITATION", ImageFont.truetype(jakarta_medium, 16), "#B5AFA6", W2, 4)

# Emerging from fade
draw_spaced_text(draw2, 1080, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 19), GOLD_LIGHT, W2, 6)
draw_centered_text(draw2, 1125, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 94), WHITE, W2)
draw_spaced_text(draw2, 1250, "CORDIALLY INVITE YOU TO CELEBRATE THEIR UNION", ImageFont.truetype(cinzel_regular, 18), "#D6D1C7", W2, 4)

draw_gold_divider(draw2, 1315, W2, 260, GOLD_PRIMARY)

draw_spaced_text(draw2, 1360, "SATURDAY", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W2, 8)
draw_centered_text(draw2, 1405, "9th January 2027", ImageFont.truetype(playfair_regular, 60), WHITE, W2)

draw_spaced_text(draw2, 1500, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 30), GOLD_LIGHT, W2, 6)
draw_spaced_text(draw2, 1545, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W2, 4)

draw_spaced_text(draw2, 1615, "ATTIRE: A BLOSSOMING ENCHANTED FOREST", ImageFont.truetype(cinzel_regular, 17), GOLD_LIGHT, W2, 4)
draw_spaced_text(draw2, 1650, "CELEBRATION DINNER & DANCING TO FOLLOW", ImageFont.truetype(jakarta_medium, 16), "#B5AFA6", W2, 3)

draw2.line([(W2 - 180) // 2, 1715, (W2 + 180) // 2, 1715], fill=GOLD_DEEP, width=1)
draw_spaced_text(draw2, 1745, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 18), GOLD_LIGHT, W2, 3)
draw_spaced_text(draw2, 1790, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 20), WHITE, W2, 5)

card2.save(os.path.join(output_dir, "Invitation-2-EnchantedEmerald-Story.png"), quality=95)
print("Saved Card 2.")


# ==============================================================================
# CARD 3: "THE HAUTE COUTURE POSTCARD" (Landscape Postcard — WhatsApp Optimized)
# 1600 x 1066 (Landscape 3:2)
# ==============================================================================
print("3/4 Generating Card 3: The Haute Couture Postcard (1600x1066)...")
W3, H3 = 1600, 1066
card3 = Image.new("RGB", (W3, H3), ALABASTER)
draw3 = ImageDraw.Draw(card3)

# Double Gold Outer Border
draw3.rectangle([28, 28, W3 - 28, H3 - 28], outline=GOLD_PRIMARY, width=2)
draw3.rectangle([36, 36, W3 - 36, H3 - 36], outline=IVORY_BORDER, width=1)
draw_ornate_corners(draw3, 44, 44, W3 - 44, H3 - 44, size=24, color=GOLD_PRIMARY)

# Left Side: Framed Photo (Seated Queen, Standing King)
pw3 = 680
ph3 = 946
px3 = 60
py3 = 60

photo3_raw = Image.open(os.path.join(images_dir, "seated-queen-standing-king.webp")).convert("RGBA")
scale3 = max(pw3 / photo3_raw.width, ph3 / photo3_raw.height)
photo3_scaled = photo3_raw.resize((int(photo3_raw.width * scale3), int(photo3_raw.height * scale3)), Image.Resampling.LANCZOS)
cx3 = (photo3_scaled.width - pw3) // 2
cy3 = int((photo3_scaled.height - ph3) * 0.15)
photo3_cropped = photo3_scaled.crop((cx3, cy3, cx3 + pw3, cy3 + ph3))

card3.paste(photo3_cropped, (px3, py3))
draw3.rectangle([px3, py3, px3 + pw3, py3 + ph3], outline=GOLD_PRIMARY, width=2)
draw3.rectangle([px3 + 6, py3 + 6, px3 + pw3 - 6, py3 + ph3 - 6], outline=IVORY_BORDER, width=1)

# Right Side: Formal Invitation Text Panel
rx0 = 780
rw = W3 - rx0 - 60
center_rx = rx0 + rw // 2

# Crest
crest_w3 = 110
crest_h3 = int(crest_raw.height * (crest_w3 / crest_raw.width))
crest_scaled3 = crest_raw.resize((crest_w3, crest_h3), Image.Resampling.LANCZOS)
card3.paste(crest_scaled3, (center_rx - crest_w3 // 2, 75), crest_scaled3)

def draw_panel_spaced(draw, y, text, font, fill, center_x, letter_spacing=5):
    total_w = sum(draw.textbbox((0,0), char, font=font)[2] - draw.textbbox((0,0), char, font=font)[0] + letter_spacing for char in text) - letter_spacing
    x = center_x - total_w // 2
    for char in text:
        draw.text((x, y), char, font=font, fill=fill)
        x += (draw.textbbox((0,0), char, font=font)[2] - draw.textbbox((0,0), char, font=font)[0]) + letter_spacing
    bbox = draw.textbbox((0,0), "A", font=font)
    return y + (bbox[3] - bbox[1])

def draw_panel_centered(draw, y, text, font, fill, center_x):
    bbox = draw.textbbox((0,0), text, font=font)
    x = center_x - (bbox[2] - bbox[0]) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return y + (bbox[3] - bbox[1])

draw_panel_spaced(draw3, 245, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 18), "#7D7565", center_rx, 5)
draw_panel_centered(draw3, 280, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 76), CHARCOAL, center_rx)
draw_panel_spaced(draw3, 385, "INVITE YOU TO CELEBRATE", ImageFont.truetype(cinzel_regular, 16), "#7D7565", center_rx, 4)
draw_panel_spaced(draw3, 415, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 26), GOLD_DEEP, center_rx, 6)

# Divider
dw3 = 200
draw3.line([center_rx - dw3//2, 475, center_rx + dw3//2, 475], fill=GOLD_PRIMARY, width=1)
draw3.polygon([(center_rx, 471), (center_rx+4, 475), (center_rx, 479), (center_rx-4, 475)], fill=GOLD_PRIMARY)

draw_panel_spaced(draw3, 510, "SATURDAY", ImageFont.truetype(cinzel_regular, 22), GOLD_PRIMARY, center_rx, 6)
draw_panel_centered(draw3, 545, "9th January 2027", ImageFont.truetype(playfair_regular, 54), CHARCOAL, center_rx)
draw_panel_spaced(draw3, 625, "AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 16), CHARCOAL_MUTED, center_rx, 3)

draw_panel_spaced(draw3, 680, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 28), GOLD_DEEP, center_rx, 5)
draw_panel_spaced(draw3, 725, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 20), CHARCOAL, center_rx, 4)

draw_panel_spaced(draw3, 785, "RECEPTION & DINNER TO FOLLOW", ImageFont.truetype(cinzel_regular, 16), CHARCOAL_MUTED, center_rx, 3)

draw3.line([center_rx - 140, 840, center_rx + 140, 840], fill=IVORY_BORDER, width=1)
draw_panel_spaced(draw3, 865, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 16), GOLD_DEEP, center_rx, 2)
draw_panel_spaced(draw3, 905, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 18), CHARCOAL, center_rx, 4)

card3.save(os.path.join(output_dir, "Invitation-3-HauteCouture-Postcard.png"), quality=95)
print("Saved Card 3.")


# ==============================================================================
# CARD 4: "THE PROPOSAL ROMANCE" (Square 1200 x 1200 — Classic Monogram Medallion)
# 1200 x 1200 (Square 1:1)
# ==============================================================================
print("4/4 Generating Card 4: The Proposal Romance (1200x1200)...")
W4, H4 = 1200, 1200
card4 = Image.new("RGB", (W4, H4), ALABASTER)
draw4 = ImageDraw.Draw(card4)

draw4.rectangle([28, 28, W4 - 28, H4 - 28], outline=GOLD_PRIMARY, width=2)
draw4.rectangle([36, 36, W4 - 36, H4 - 36], outline=IVORY_BORDER, width=1)
draw_ornate_corners(draw4, 44, 44, W4 - 44, H4 - 44, size=22, color=GOLD_PRIMARY)

# Circular Medallion Photo (Photo 0844 or Seated Queen)
mw4 = 420
mx4 = (W4 - mw4) // 2
my4 = 65

photo4_raw = Image.open(os.path.join(images_dir, "IMG_0844.webp")).convert("RGBA")
scale4 = max(mw4 / photo4_raw.width, mw4 / photo4_raw.height)
photo4_scaled = photo4_raw.resize((int(photo4_raw.width * scale4), int(photo4_raw.height * scale4)), Image.Resampling.LANCZOS)
cx4 = (photo4_scaled.width - mw4) // 2
cy4 = (photo4_scaled.height - mw4) // 2
photo4_cropped = photo4_scaled.crop((cx4, cy4, cx4 + mw4, cy4 + mw4))

circle_mask = Image.new("L", (mw4, mw4), 0)
draw_cm = ImageDraw.Draw(circle_mask)
draw_cm.ellipse([0, 0, mw4, mw4], fill=255)

card4.paste(photo4_cropped, (mx4, my4), circle_mask)

# Outer Gold Circle Frame around medallion
draw4.ellipse([mx4 - 4, my4 - 4, mx4 + mw4 + 4, my4 + mw4 + 4], outline=GOLD_PRIMARY, width=2)
draw4.ellipse([mx4 - 8, my4 - 8, mx4 + mw4 + 8, my4 + mw4 + 8], outline=IVORY_BORDER, width=1)

# Typography below
draw_spaced_text(draw4, 530, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 19), "#7D7565", W4, 5)
draw_centered_text(draw4, 570, "Kevin & Shannel", ImageFont.truetype(playfair_italic, 88), CHARCOAL, W4)
draw_spaced_text(draw4, 680, "REQUEST THE HONOUR OF YOUR COMPANY AT", ImageFont.truetype(cinzel_regular, 17), "#7D7565", W4, 4)
draw_spaced_text(draw4, 715, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 28), GOLD_DEEP, W4, 7)

draw_gold_divider(draw4, 780, W4, 240, GOLD_PRIMARY)

draw_spaced_text(draw4, 820, "SATURDAY, 9TH JANUARY 2027", ImageFont.truetype(cinzel_regular, 24), GOLD_PRIMARY, W4, 6)
draw_spaced_text(draw4, 865, "CEREMONY AT ONE O'CLOCK • RECEPTION TO FOLLOW", ImageFont.truetype(cinzel_regular, 17), CHARCOAL_MUTED, W4, 3)

draw_spaced_text(draw4, 925, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(cinzel_regular, 26), CHARCOAL, W4, 5)

draw4.line([(W4 - 180) // 2, 995, (W4 + 180) // 2, 995], fill=IVORY_BORDER, width=1)
draw_spaced_text(draw4, 1025, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 18), GOLD_DEEP, W4, 3)
draw_spaced_text(draw4, 1070, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 20), CHARCOAL, W4, 5)

card4.save(os.path.join(output_dir, "Invitation-4-ProposalRomance-Square.png"), quality=95)
print("Saved Card 4.")

print("All 4 Formal Invitation Cards Generated Successfully!")
