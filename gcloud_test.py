import os

from dotenv import load_dotenv
from google.cloud import texttospeech

# requires service account credentials path in .env
load_dotenv()

tts_client = texttospeech.TextToSpeechClient()


def get_tts(output_path: str, input_text: str, filename: str):
    gc_input_text = texttospeech.SynthesisInput(text=input_text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = tts_client.synthesize_speech(
        request={"input": gc_input_text, "voice": voice, "audio_config": audio_config}
    )

    filepath = os.path.join(output_path, f"{filename}.mp3")
    with open(filepath, "wb") as out:
        out.write(response.audio_content)


if __name__ == '__main__':
    txt_response = str(tts_client.list_voices(language_code="en-US"))
    print(txt_response.count("Wavenet"))
    # print(txt_response)

