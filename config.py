import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

SCRIPT_PATH = os.path.join(DATA_DIR, "script.txt")
AUDIO_PATH = os.path.join(DATA_DIR, "voice.wav")
IMAGE_PATH = os.path.join(DATA_DIR, "image.jpg")

VIDEO_OUTPUT = os.path.join(OUTPUT_DIR, "video.mp4")

PROMPT = "Discipline, consistency, and success mindset"