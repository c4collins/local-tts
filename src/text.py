import re

import os
import sys

if getattr(sys, "frozen", False):
    # for executable mode
    BASE_DIR = sys._MEIPASS
else:
    # for development mode
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def replace_bad_words(input_text):
    replacement_text = input_text
    with open(
        os.path.join(BASE_DIR, "data", "text_to_replace.csv"), "r"
    ) as bad_word_file:
        for line in bad_word_file.readlines():
            from_text, to_text = line.split(",")
            replacement_text = re.sub(
                rf"\b{from_text.strip()}\b", to_text.strip(), replacement_text
            )

    return replacement_text


def replace_special_characters(raw_tts):
    replaced_tts = raw_tts  # .encode('ascii', 'ignore').decode('utf-8')
    replaced_tts = re.sub("[\W_\d]+", " ", replaced_tts)
    replaced_tts = replaced_tts.replace("%0A", "; ")
    replaced_tts = replaced_tts.replace("â€™", "'")
    replaced_tts = replaced_tts.replace("‘", "'")
    replaced_tts = replaced_tts.replace("`", "'")
    replaced_tts = replaced_tts.replace("â€˜", "'")
    replaced_tts = replaced_tts.replace("%22", '"')

    return replaced_tts
