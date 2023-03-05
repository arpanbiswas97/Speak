import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import argparse
from io import BytesIO

import gtts
import pygame


def speak(text: str):
    """Speaks the text out loud using Google Text-to-Speech

    Parameters
    ----------
    text : str
        The text to speak

    Returns
    -------
    None
    """
    tts = gtts.gTTS(text, lang="en", tld="us")
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
        pass


def main():
    parser = argparse.ArgumentParser("speak", description="Speaks the text out loud using Google Text-to-Speech")
    parser.add_argument("text")
    args = parser.parse_args()

    text = args.text
    speak(text)


if __name__ == "__main__":
    main()
