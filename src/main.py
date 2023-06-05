import argparse

from tts import say, listen_to_voices
from text import replace_bad_words, replace_special_characters

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--voice",
        help="Voice (use -V to see available voices)",
        required=False,
        default=1,
    )
    parser.add_argument("-r", "--rate", help="Read speed", required=False, default=145)
    parser.add_argument(
        "-m", "--message", help="The first T in TTS", default="Hello, World!"
    )
    parser.add_argument(
        "-V", "--voices", help="Hear the available voices", action="store_true"
    )

    args = parser.parse_args()
    rate = int(args.rate) if args.rate else 145

    if not args.voices:
        voice = int(args.voice) if args.voice else 1

        tts_without_special_characters = replace_special_characters(args.message)
        to_say = replace_bad_words(tts_without_special_characters)
        say(to_say, voice, rate)

    else:
        listen_to_voices(rate)
