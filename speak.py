import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import argparse
from io import BytesIO

import gtts
import pygame

LANGUAGE_MAPPINGS = {
    "english": {
        "local": ("en", "com"),
        "au": ("en", "com.au"),
        "uk": ("en", "co.uk"),
        "us": ("en", "us"),
        "ca": ("en", "ca"),
        "in": ("en", "co.in"),
        "ie": ("en", "ie"),
        "za": ("en", "co.za"),
    },
    "french": {
        "local": ("fr", "com"),
        "ca": ("fr", "ca"),
        "fr": ("fr", "fr"),
    },
    "mandarin": {
        "cn": ("zh-CN", "com"),
        "tw": ("zh-TW", "com"),
    },
    "portuguese": {
        "local": ("pt", "com"),
        "br": ("pt", "com.br"),
        "pt": ("pt", "pt"),
    },
    "spanish": {
        "local": ("es", "com"),
        "es": ("es", "es"),
        "mx": ("es", "com.mx"),
        "us": ("es", "us"),
    },
}


def speak(text: str, language: str = "english", variant: str = "local"):
    """Speak the text out loud using Google Text-to-Speech.

    Parameters
    ----------
    text : str
        Text to speak.
    language : str, optional
        Language to use, by default "english"
    variant : str, optional
        Language variant to use, by default "local"
    """

    if language not in LANGUAGE_MAPPINGS:
        raise ValueError(
            f"Invalid language: {language}. Valid languages are: {list(LANGUAGE_MAPPINGS.keys())}"
        )
    if variant not in LANGUAGE_MAPPINGS[language]:
        raise ValueError(
            f"Invalid variant: {variant} for language {language}. Valid variants are: {list(LANGUAGE_MAPPINGS[language].keys())}"
        )
    lang, tld = LANGUAGE_MAPPINGS[language][variant]

    tts = gtts.gTTS(text, lang=lang, tld=tld)
    mp3_fp = BytesIO()  # In-memory file-like object
    tts.write_to_fp(mp3_fp)  # Write the mp3 data to the file-like object
    mp3_fp.seek(0)

    # Play the mp3 file
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "speak", description="Speaks the text out loud using Google Text-to-Speech"
    )
    parser.add_argument("text")
    parser.add_argument(
        "-l",
        "--language",
        default="english",
        help="Language to use (default: english)",
        type=str,
        choices=LANGUAGE_MAPPINGS.keys(),
    )
    parser.add_argument(
        "-v",
        "--variant",
        default="local",
        help="Language variant to use (default: local)",
        type=str,
        choices=set([k for d in LANGUAGE_MAPPINGS.values() for k in d.keys()]),
    )
    args = parser.parse_args()

    text = args.text
    language = args.language
    variant = args.variant

    speak(text, language, variant)
