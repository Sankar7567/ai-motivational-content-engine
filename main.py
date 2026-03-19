import os

from config import *
from engines.script_engine import generate_content
from engines.image_engine import generate_image
from engines.tts_engine import text_to_speech
from engines.video_engine import create_video
from engines.shorts_engine import create_short


def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_user_input():
    mode = input("Enter mode (short / long): ").strip().lower()
    duration = int(input("Enter duration in minutes (e.g. 1, 5, 10): ").strip())
    return mode, duration


def main():
    ensure_dirs()

    print("\n🚀 AI Content Engine v2\n")

    mode, duration = get_user_input()

    print("\n⚙️ Generating content...\n")

    content = generate_content(PROMPT, duration, mode)

    script = content.get("script", "")
    image_prompt = content.get("image_prompt", "")
    title = content.get("title", "")
    description = content.get("description", "")
    hashtags = content.get("hashtags", "")
    thumbnail = content.get("thumbnail_text", "")

    # Save script
    with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(script)

    # Print everything
    print("\n🎬 TITLE:\n", title)
    print("\n📝 DESCRIPTION:\n", description)
    print("\n🏷️ HASHTAGS:\n", hashtags)
    print("\n🖼️ THUMBNAIL TEXT:\n", thumbnail)

    print("\n📜 SCRIPT PREVIEW:\n", script[:200], "...")

    # Save metadata
    meta_path = os.path.join(DATA_DIR, "meta.txt")
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(
            f"TITLE:\n{title}\n\nDESCRIPTION:\n{description}\n\nHASHTAGS:\n{hashtags}\n\nTHUMBNAIL:\n{thumbnail}"
        )

    print("\n💾 Metadata saved")

    # Generate assets
    image_path = generate_image(image_prompt)
    audio_path = text_to_speech(script, AUDIO_PATH)

    # Create main video
    video_path = create_video(image_path, audio_path)

    print("\n🎬 Main video done:", video_path)

    # Create short if long mode
    if mode == "long":
        short_path = create_short(video_path)
        print("📱 Short created:", short_path)

    print("\n🎉 ALL DONE!")


if __name__ == "__main__":
    main()