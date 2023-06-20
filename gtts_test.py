from gtts import gTTS
import os


def get_tts(output_path: str, input_text: str, filename: str):
    tts = gTTS(input_text, lang='en')
    tts.save(os.path.join(output_path, f"{filename}.mp3"))


def test():
    tts = gTTS('hello', lang='en')
    tts.save('hello.mp3')


if __name__ == '__main__':
    test()
