import subprocess
from config import VIDEO_OUTPUT

FFMPEG_PATH = r"C:\Users\Kittu\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"

def create_video(image_path, audio_path):
    command = [
        FFMPEG_PATH,
        "-y",  # overwrite
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        VIDEO_OUTPUT
    ]

    subprocess.run(command, check=True)

    return VIDEO_OUTPUT