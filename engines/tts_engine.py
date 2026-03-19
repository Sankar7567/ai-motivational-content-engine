import asyncio
import edge_tts

VOICE = "en-US-GuyNeural"  # 🔥 natural male voice

async def generate_audio(text, output_path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_path)

def text_to_speech(text, output_path):
    asyncio.run(generate_audio(text, output_path))
    return output_path