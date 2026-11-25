from PIL import Image, ImageDraw, ImageFilter
import os, random, math

random.seed(42)

def make_xray(label, idx):
    img = Image.new('RGB', (256, 256), (8, 8, 8))
    draw = ImageDraw.Draw(img)
    # Spine
    for y in range(50, 220, 15):
        draw.rectangle([120, y, 134, y+10], fill=(90, 90, 90))
    # Left lung
    draw.ellipse([35, 55, 115, 200], outline=(160, 160, 160), width=3)
    # Right lung
    draw.ellipse([140, 55, 220, 200], outline=(160, 160, 160), width=3)
    # Ribs
    for y in [75, 95, 115, 135, 155, 175]:
        draw.arc([30, y-15, 240, y+20], 0, 180, fill=(110, 110, 110), width=1)
    # Heart
    draw.ellipse([100, 100, 155, 165], fill=(50, 50, 50), outline=(80, 80, 80))
    # Abnormal finding
    if label == 'Abnormal':
        x = random.randint(45, 95)
        y = random.randint(80, 170)
        r = random.randint(8, 18)
        draw.ellipse([x, y, x+r*2, y+r*2], fill=(200, 200, 200))
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    return img

def make_mri(tumor_type, idx):
    img = Image.new('RGB', (256, 256), (5, 5, 5))
    draw = ImageDraw.Draw(img)
    # Skull
    draw.ellipse([20, 20, 235, 235], fill=(40, 40, 40), outline=(120, 120, 120), width=3)
    # Brain matter
    draw.ellipse([35, 35, 220, 220], fill=(95, 90, 85))
    # Ventricles
    draw.ellipse([110, 105, 145, 150], fill=(30, 30, 30))
    # Folds/gyri
    for a in range(0, 360, 45):
        rad = math.radians(a)
        x1 = int(128 + 70*math.cos(rad))
        y1 = int(128 + 70*math.sin(rad))
        x2 = int(128 + 85*math.cos(rad+0.3))
        y2 = int(128 + 85*math.sin(rad+0.3))
        draw.line([(x1,y1),(x2,y2)], fill=(75,70,65), width=2)
    # Tumor
    if tumor_type == 'glioma':
        draw.ellipse([80, 80, 130, 130], fill=(180, 60, 60))
    elif tumor_type == 'meningioma':
        cx, cy, r = 128, 40, 18
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(60, 180, 60))
    elif tumor_type == 'pituitary':
        draw.ellipse([115, 150, 140, 175], fill=(60, 60, 200))
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    return img

for d in ['data/xray/sample/Normal','data/xray/sample/Abnormal',
          'data/mri/sample/glioma','data/mri/sample/meningioma',
          'data/mri/sample/pituitary','data/mri/sample/no_tumor']:
    os.makedirs(d, exist_ok=True)

for i in range(5):
    make_xray('Normal', i).save(f'data/xray/sample/Normal/normal_{i:03d}.png')
    make_xray('Abnormal', i).save(f'data/xray/sample/Abnormal/abnormal_{i:03d}.png')
    for t in ['glioma','meningioma','pituitary','no_tumor']:
        make_mri(t, i).save(f'data/mri/sample/{t}/{t}_{i:03d}.png')

print("Done. Sample images created.")
