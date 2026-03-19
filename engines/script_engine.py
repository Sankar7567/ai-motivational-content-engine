import requests
import json

def generate_content(prompt, duration, mode):
    url = "http://localhost:11434/api/generate"

    full_prompt = f"""
    You are a motivational content generator.

    ONLY return valid JSON. No explanation.

    Generate:
    - script (~{duration} minutes)
    - image_prompt
    - title
    - description
    - hashtags
    - thumbnail_text

    Topic: {prompt}

    JSON FORMAT:
    {{
        "script": "...",
        "image_prompt": "...",
        "title": "...",
        "description": "...",
        "hashtags": "...",
        "thumbnail_text": "..."
    }}
    """

    response = requests.post(url, json={
        "model": "deepseek-r1:8b",
        "prompt": full_prompt,
        "stream": False
    })

    text = response.json().get("response", "").strip()

    # 🔥 DEBUG PRINT (important)
    print("\n🧠 RAW MODEL OUTPUT:\n", text[:500], "\n")

    # 🔥 SAFE JSON EXTRACTION
    try:
        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("No JSON found")

        json_text = text[start:end]

        return json.loads(json_text)

    except Exception as e:
        print("❌ JSON parsing failed:", e)

        # 🔥 FALLBACK (never crash system)
        return {
            "script": "Discipline is the key to success. Keep going.",
            "image_prompt": "motivational dark background, cinematic",
            "title": "Stay Disciplined",
            "description": "Push yourself beyond limits.",
            "hashtags": "#motivation #discipline #success",
            "thumbnail_text": "STAY HARD"
        }