import os
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate, save, voices

load_dotenv()
set_api_key(os.getenv("XI_API_KEY"))


def get_tts(output_path: str, input_text: str, filename: str):
    audio = generate(
        text=input_text,
        voice="Rachel",
        model="eleven_monolingual_v1"
    )
    save(audio, os.path.join(output_path, f"{filename}.mp3"))


if __name__ == '__main__':
    print(voices())
