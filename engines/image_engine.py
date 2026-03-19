import requests
from config import IMAGE_PATH
from PIL import Image
import random

def generate_image(prompt):
    try:
        # 🔥 Using picsum (free, no API key, always works)
        url = f"https://picsum.photos/1280/720?random={random.randint(1,10000)}"

        img_data = requests.get(url, timeout=10).content

        with open(IMAGE_PATH, "wb") as f:
            f.write(img_data)

        print("✅ Image fetched (free source)")
        return IMAGE_PATH

    except Exception as e:
        print("❌ Image error:", e)
        return fallback_image()


def fallback_image():
    img = Image.new("RGB", (1280, 720), color=(0, 0, 0))
    img.save(IMAGE_PATH)
    print("⚠️ Fallback image used")
    return IMAGE_PATH