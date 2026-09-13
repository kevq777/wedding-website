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

# Color Tokens
GOLD_PRIMARY = "#C5A059"
GOLD_LIGHT = "#E8C88B"
GOLD_DEEP = "#9E7A33"
GOLD_ACCENT = "#D4AF37"
CHARCOAL = "#1A1918"
CHARCOAL_MUTED = "#524D44"
CHARCOAL_LIGHT = "#787267"
WHITE = "#FFFFFF"
ALABASTER = "#FAF7F2"
IVORY_BORDER = "#E8E1D3"
EMERALD_NOIR = "#0A1711"
OBSIDIAN_NOIR = "#131314"

def draw_centered_text(draw, y, text, font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return y + (bbox[3] - bbox[1])

def draw_spaced_text(draw, y, text, font, fill, width, letter_spacing=6):
    # Use typographic advance width via draw.textlength to avoid unnatural gaps after glyphs like 'Q'
    char_widths = [draw.textlength(char, font=font) for char in text]
    total_w = sum(char_widths) + letter_spacing * (len(text) - 1)
    x = (width - total_w) / 2.0
    for char, cw in zip(text, char_widths):
        draw.text((x, y), char, font=font, fill=fill)
        x += cw + letter_spacing
    bbox = draw.textbbox((0,0), "A", font=font)
    return y + (bbox[3] - bbox[1])

def draw_gold_divider(draw, y, width, line_width=260, color=GOLD_PRIMARY):
    dx = (width - line_width) // 2
    draw.line([dx, y, dx + line_width, y], fill=color, width=1)
    cx = width // 2
    draw.polygon([(cx, y-5), (cx+5, y), (cx, y+5), (cx-5, y)], fill=color)

def draw_ornate_corners(draw, x0, y0, x1, y1, size=32, color=GOLD_PRIMARY):
    # Top Left
    draw.line([x0, y0 + size, x0, y0, x0 + size, y0], fill=color, width=2)
    draw.line([x0 + 6, y0 + size - 6, x0 + 6, y0 + 6, x0 + size - 6, y0 + 6], fill=color, width=1)
    # Top Right
    draw.line([x1 - size, y0, x1, y0, x1, y0 + size], fill=color, width=2)
    draw.line([x1 - size + 6, y0 + 6, x1 - 6, y0 + 6, x1 - 6, y0 + size - 6], fill=color, width=1)
    # Bottom Left
    draw.line([x0, y1 - size, x0, y1, x0 + size, y1], fill=color, width=2)
    draw.line([x0 + 6, y1 - size + 6, x0 + 6, y1 - 6, x0 + size - 6, y1 - 6], fill=color, width=1)
    # Bottom Right
    draw.line([x1 - size, y1, x1, y1, x1, y1 - size], fill=color, width=2)
    draw.line([x1 - size + 6, y1 - 6, x1 - 6, y1 - 6, x1 - 6, y1 - size + 6], fill=color, width=1)

crest_raw_gold = Image.open(os.path.join(images_dir, "ks-crest-gold.png")).convert("RGBA")
crest_raw_charcoal = Image.open(os.path.join(images_dir, "ks-crest-charcoal.png")).convert("RGBA")

# Build a rich burnished antique gold crest specifically for light alabaster paper
def create_burnished_gold_crest():
    _, _, _, a = crest_raw_charcoal.split()
    gold_fill = Image.new("RGBA", crest_raw_charcoal.size, (178, 140, 72, 255))
    gold_fill.putalpha(a)
    return gold_fill

crest_antique_gold = create_burnished_gold_crest()

# ==============================================================================
# CARD 1: "THE ROYAL ALABASTER & GOLD" (Pure Typographic Luxury)
# Portrait 9:16 (1080 x 1920)
# ==============================================================================
print("1/4 Generating Card 1: The Royal Alabaster (Full Names, No Photo)...")
W1, H1 = 1080, 1920
card1 = Image.new("RGB", (W1, H1), ALABASTER)
draw1 = ImageDraw.Draw(card1)

# Triple Hairline Gold Border with Ornate Corners
draw1.rectangle([34, 34, W1 - 34, H1 - 34], outline=GOLD_PRIMARY, width=2)
draw1.rectangle([44, 44, W1 - 44, H1 - 44], outline=IVORY_BORDER, width=1)
draw1.rectangle([56, 56, W1 - 56, H1 - 56], outline=GOLD_PRIMARY, width=1)
draw_ornate_corners(draw1, 68, 68, W1 - 68, H1 - 68, size=36, color=GOLD_PRIMARY)

# Prominent Burnished Gold Monogram Crest at Top
crest_w1 = 185
crest_h1 = int(crest_antique_gold.height * (crest_w1 / crest_antique_gold.width))
crest1_scaled = crest_antique_gold.resize((crest_w1, crest_h1), Image.Resampling.LANCZOS)
card1.paste(crest1_scaled, ((W1 - crest_w1) // 2, 130), crest1_scaled)

draw_spaced_text(draw1, 425, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 24), GOLD_DEEP, W1, 8)
draw_gold_divider(draw1, 480, W1, 220, GOLD_PRIMARY)

draw_spaced_text(draw1, 535, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 20), CHARCOAL_LIGHT, W1, 6)

# Full Formal Names (Equal size 70pt)
draw_centered_text(draw1, 610, "Kevin Elikem Quist", ImageFont.truetype(playfair_italic, 70), CHARCOAL, W1)
draw_centered_text(draw1, 710, "&", ImageFont.truetype(playfair_italic, 50), GOLD_PRIMARY, W1)
draw_centered_text(draw1, 780, "Shannel Naa-Larbia Darku", ImageFont.truetype(playfair_italic, 70), CHARCOAL, W1)

draw_spaced_text(draw1, 925, "REQUEST THE HONOUR OF YOUR PRESENCE", ImageFont.truetype(cinzel_regular, 19), CHARCOAL_MUTED, W1, 4)
draw_spaced_text(draw1, 970, "TO CELEBRATE THEIR UNION BEFORE GOD", ImageFont.truetype(cinzel_regular, 19), CHARCOAL_MUTED, W1, 4)

# Scripture Quote in Center
draw_gold_divider(draw1, 1045, W1, 280, GOLD_PRIMARY)
draw_centered_text(draw1, 1090, "“I have found the one whom my soul loves.”", ImageFont.truetype(playfair_italic, 30), CHARCOAL, W1)
draw_spaced_text(draw1, 1140, "SONG OF SOLOMON 3:4", ImageFont.truetype(cinzel_regular, 16), GOLD_DEEP, W1, 4)
draw_gold_divider(draw1, 1190, W1, 280, GOLD_PRIMARY)

# Date & Timings
draw_spaced_text(draw1, 1255, "SATURDAY", ImageFont.truetype(cinzel_regular, 26), GOLD_PRIMARY, W1, 8)
draw_centered_text(draw1, 1305, "9th January 2027", ImageFont.truetype(playfair_regular, 66), CHARCOAL, W1)
draw_spaced_text(draw1, 1405, "CEREMONY AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 19), CHARCOAL_MUTED, W1, 4)

# Venue (Reception & Attire removed)
draw_spaced_text(draw1, 1490, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 34), GOLD_DEEP, W1, 6)
draw_spaced_text(draw1, 1545, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), CHARCOAL, W1, 5)

# RSVP and Web Address
draw1.line([(W1 - 220) // 2, 1640, (W1 + 220) // 2, 1640], fill=IVORY_BORDER, width=1)
draw_spaced_text(draw1, 1680, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 19), GOLD_DEEP, W1, 3)
draw_spaced_text(draw1, 1730, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 22), CHARCOAL, W1, 5)

card1.save(os.path.join(output_dir, "Invitation-1-RoyalAlabaster-Story.png"), quality=95)
print("Saved Card 1.")


# ==============================================================================
# CARD 2: "THE ENCHANTED FOREST EMERALD" (Deep Velvety Green & Gold Calligraphy)
# Portrait 9:16 (1080 x 1920)
# ==============================================================================
print("2/4 Generating Card 2: The Enchanted Forest Emerald (Full Names, No Photo)...")
W2, H2 = 1080, 1920
card2 = Image.new("RGB", (W2, H2), (10, 22, 17)) # Rich Forest Emerald
draw2 = ImageDraw.Draw(card2)

# Double Gold Border with Corner Brackets
draw2.rectangle([34, 34, W2 - 34, H2 - 34], outline=GOLD_PRIMARY, width=2)
draw2.rectangle([46, 46, W2 - 46, H2 - 46], outline=GOLD_DEEP, width=1)
draw_ornate_corners(draw2, 58, 58, W2 - 58, H2 - 58, size=34, color=GOLD_LIGHT)

# Luminous Gold Crest at Top
crest2_scaled = crest_raw_gold.resize((crest_w1, crest_h1), Image.Resampling.LANCZOS)
card2.paste(crest2_scaled, ((W2 - crest_w1) // 2, 130), crest2_scaled)

draw_spaced_text(draw2, 425, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 24), GOLD_LIGHT, W2, 8)
draw_gold_divider(draw2, 480, W2, 220, GOLD_LIGHT)

draw_spaced_text(draw2, 535, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 20), "#B5AFA6", W2, 6)

# Full Formal Names (Equal size 70pt)
draw_centered_text(draw2, 610, "Kevin Elikem Quist", ImageFont.truetype(playfair_italic, 70), WHITE, W2)
draw_centered_text(draw2, 710, "&", ImageFont.truetype(playfair_italic, 50), GOLD_LIGHT, W2)
draw_centered_text(draw2, 780, "Shannel Naa-Larbia Darku", ImageFont.truetype(playfair_italic, 70), WHITE, W2)

draw_spaced_text(draw2, 925, "REQUEST THE HONOUR OF YOUR PRESENCE", ImageFont.truetype(cinzel_regular, 19), "#D1CCC2", W2, 4)
draw_spaced_text(draw2, 970, "TO WITNESS THEIR SACRED VOWS", ImageFont.truetype(cinzel_regular, 19), "#D1CCC2", W2, 4)

# Scripture Quote in Center
draw_gold_divider(draw2, 1045, W2, 280, GOLD_LIGHT)
draw_centered_text(draw2, 1090, "“I have found the one whom my soul loves.”", ImageFont.truetype(playfair_italic, 30), GOLD_LIGHT, W2)
draw_spaced_text(draw2, 1140, "SONG OF SOLOMON 3:4", ImageFont.truetype(cinzel_regular, 16), "#B5AFA6", W2, 4)
draw_gold_divider(draw2, 1190, W2, 280, GOLD_LIGHT)

# Date & Timings
draw_spaced_text(draw2, 1255, "SATURDAY", ImageFont.truetype(cinzel_regular, 26), GOLD_LIGHT, W2, 8)
draw_centered_text(draw2, 1305, "9th January 2027", ImageFont.truetype(playfair_regular, 66), WHITE, W2)
draw_spaced_text(draw2, 1405, "CEREMONY AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 19), "#D1CCC2", W2, 4)

# Venue (Reception & Attire removed)
draw_spaced_text(draw2, 1490, "LABADI BEACH HOTEL", ImageFont.truetype(cinzel_regular, 34), GOLD_LIGHT, W2, 6)
draw_spaced_text(draw2, 1545, "ACCRA, GHANA", ImageFont.truetype(jakarta_medium, 22), WHITE, W2, 5)

# RSVP and Web Address
draw2.line([(W2 - 220) // 2, 1640, (W2 + 220) // 2, 1640], fill=GOLD_DEEP, width=1)
draw_spaced_text(draw2, 1680, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 19), GOLD_LIGHT, W2, 3)
draw_spaced_text(draw2, 1730, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 22), WHITE, W2, 5)

card2.save(os.path.join(output_dir, "Invitation-2-EnchantedEmerald-Story.png"), quality=95)
print("Saved Card 2.")


# ==============================================================================
# CARD 3: "THE CLASSICAL POSTCARD" (Traditional Formal Landscape Invitation)
# Landscape 3:2 (1600 x 1066)
# ==============================================================================
print("3/4 Generating Card 3: The Classical Postcard (Full Names, No Photo)...")
W3, H3 = 1600, 1066
card3 = Image.new("RGB", (W3, H3), ALABASTER)
draw3 = ImageDraw.Draw(card3)

# Double Gold Outer Border with Corner Accents
draw3.rectangle([32, 32, W3 - 32, H3 - 32], outline=GOLD_PRIMARY, width=2)
draw3.rectangle([42, 42, W3 - 42, H3 - 42], outline=IVORY_BORDER, width=1)
draw3.rectangle([52, 52, W3 - 52, H3 - 52], outline=GOLD_PRIMARY, width=1)
draw_ornate_corners(draw3, 62, 62, W3 - 62, H3 - 62, size=32, color=GOLD_PRIMARY)

# Centered Burnished Gold Crest at Top
crest_w3 = 140
crest_h3 = int(crest_antique_gold.height * (crest_w3 / crest_antique_gold.width))
crest3_scaled = crest_antique_gold.resize((crest_w3, crest_h3), Image.Resampling.LANCZOS)
card3.paste(crest3_scaled, ((W3 - crest_w3) // 2, 75), crest3_scaled)

draw_spaced_text(draw3, 290, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 22), GOLD_DEEP, W3, 8)
draw_gold_divider(draw3, 335, W3, 220, GOLD_PRIMARY)

draw_spaced_text(draw3, 370, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 18), CHARCOAL_LIGHT, W3, 6)

# Couple Full Names with Gold Ampersand (Size 48pt for complete names)
name_f3 = ImageFont.truetype(playfair_italic, 48)
amp_f3 = ImageFont.truetype(playfair_italic, 40)
w_kq = draw3.textlength("Kevin Elikem Quist", font=name_f3)
w_amp = draw3.textlength(" & ", font=amp_f3)
w_snd = draw3.textlength("Shannel Naa-Larbia Darku", font=name_f3)
total_names_w = w_kq + w_amp + w_snd
start_x3 = (W3 - total_names_w) / 2.0
y_name3 = 425
draw3.text((start_x3, y_name3), "Kevin Elikem Quist", font=name_f3, fill=CHARCOAL)
draw3.text((start_x3 + w_kq, y_name3 + 4), " & ", font=amp_f3, fill=GOLD_PRIMARY)
draw3.text((start_x3 + w_kq + w_amp, y_name3), "Shannel Naa-Larbia Darku", font=name_f3, fill=CHARCOAL)

draw_spaced_text(draw3, 525, "REQUEST THE HONOUR OF YOUR PRESENCE AT THEIR WEDDING CELEBRATION", ImageFont.truetype(cinzel_regular, 18), CHARCOAL_MUTED, W3, 4)

draw_gold_divider(draw3, 585, W3, 300, GOLD_PRIMARY)

draw_spaced_text(draw3, 630, "SATURDAY, 9TH JANUARY 2027", ImageFont.truetype(cinzel_regular, 24), GOLD_PRIMARY, W3, 7)
draw_spaced_text(draw3, 675, "CEREMONY AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 18), CHARCOAL_MUTED, W3, 4)

draw_spaced_text(draw3, 745, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(cinzel_regular, 28), CHARCOAL, W3, 6)

draw3.line([(W3 - 240) // 2, 835, (W3 + 240) // 2, 835], fill=IVORY_BORDER, width=1)
draw_spaced_text(draw3, 870, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 18), GOLD_DEEP, W3, 3)
draw_spaced_text(draw3, 915, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 20), CHARCOAL, W3, 5)

card3.save(os.path.join(output_dir, "Invitation-3-HauteCouture-Postcard.png"), quality=95)
print("Saved Card 3.")


# ==============================================================================
# CARD 4: "THE ROYAL OBSIDIAN NOIR" (Square 1200 x 1200 — Gold Foil Stamping)
# Square 1:1 (1200 x 1200)
# ==============================================================================
print("4/4 Generating Card 4: The Royal Obsidian Noir (Full Names, No Photo)...")
W4, H4 = 1200, 1200
card4 = Image.new("RGB", (W4, H4), OBSIDIAN_NOIR)
draw4 = ImageDraw.Draw(card4)

# Double Gold Outer Border
draw4.rectangle([32, 32, W4 - 32, H4 - 32], outline=GOLD_PRIMARY, width=2)
draw4.rectangle([42, 42, W4 - 42, H4 - 42], outline=GOLD_DEEP, width=1)
draw_ornate_corners(draw4, 52, 52, W4 - 52, H4 - 52, size=30, color=GOLD_LIGHT)

# Luminous Gold Crest
crest_w4 = 150
crest_h4 = int(crest_raw_gold.height * (crest_w4 / crest_raw_gold.width))
crest4_scaled = crest_raw_gold.resize((crest_w4, crest_h4), Image.Resampling.LANCZOS)
card4.paste(crest4_scaled, ((W4 - crest_w4) // 2, 85), crest4_scaled)

draw_spaced_text(draw4, 315, "THE WHITE WEDDING", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W4, 8)
draw_gold_divider(draw4, 360, W4, 200, GOLD_LIGHT)

draw_spaced_text(draw4, 400, "TOGETHER WITH THEIR FAMILIES", ImageFont.truetype(cinzel_regular, 18), "#A69F94", W4, 5)

# Both names size 58 for square balance
draw_centered_text(draw4, 460, "Kevin Elikem Quist", ImageFont.truetype(playfair_italic, 58), WHITE, W4)
draw_centered_text(draw4, 540, "&", ImageFont.truetype(playfair_italic, 44), GOLD_LIGHT, W4)
draw_centered_text(draw4, 600, "Shannel Naa-Larbia Darku", ImageFont.truetype(playfair_italic, 58), WHITE, W4)

draw_spaced_text(draw4, 710, "CORDIALLY INVITE YOU TO CELEBRATE THEIR UNION", ImageFont.truetype(cinzel_regular, 17), "#D1CCC2", W4, 4)

draw_gold_divider(draw4, 770, W4, 240, GOLD_LIGHT)

draw_spaced_text(draw4, 810, "SATURDAY, 9TH JANUARY 2027", ImageFont.truetype(cinzel_regular, 22), GOLD_LIGHT, W4, 6)
draw_spaced_text(draw4, 855, "CEREMONY AT ONE O'CLOCK IN THE AFTERNOON", ImageFont.truetype(cinzel_regular, 17), "#B5AFA6", W4, 3)

draw_spaced_text(draw4, 915, "LABADI BEACH HOTEL • ACCRA, GHANA", ImageFont.truetype(cinzel_regular, 26), WHITE, W4, 5)

draw4.line([(W4 - 180) // 2, 985, (W4 + 180) // 2, 985], fill=GOLD_DEEP, width=1)
draw_spaced_text(draw4, 1020, "KINDLY RSVP BY 1ST DECEMBER 2026", ImageFont.truetype(jakarta_medium, 18), GOLD_LIGHT, W4, 3)
draw_spaced_text(draw4, 1065, "WWW.KEVINANDSHANNEL.COM", ImageFont.truetype(cinzel_regular, 20), WHITE, W4, 5)

card4.save(os.path.join(output_dir, "Invitation-4-ProposalRomance-Square.png"), quality=95)
print("Saved Card 4.")

print("All 4 Photo-Free Formal Invitation Cards Generated Successfully!")
