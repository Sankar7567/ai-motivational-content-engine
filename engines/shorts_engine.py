import os
import subprocess
from config import OUTPUT_DIR

FFMPEG_PATH = r"C:\Users\Kittu\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"

def create_short(video_path):
    short_path = os.path.join(OUTPUT_DIR, "short.mp4")

    command = [
        FFMPEG_PATH,
        "-y",
        "-i", video_path,
        "-t", "30",  # first 30 sec
        "-vf", "scale=720:1280",  # vertical
        "-c:v", "libx264",
        "-c:a", "aac",
        short_path
    ]

    subprocess.run(command, check=True)

    return short_path