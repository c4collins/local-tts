import pyttsx3


def say(to_say, voice, rate):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice].id)

    engine.setProperty("rate", rate)

    print(to_say)
    engine.say(to_say)

    engine.runAndWait()


def listen_to_voices(rate):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    print(f"There are {len(voices)} voices available")

    engines = {}
    for i, v in enumerate(voices):
        voice_details = f"{i}) {v.name}"
        say(voice_details, i, rate)


def listen_to_voice(num, voice, text):
    engine = pyttsx3.init()
    engine.setProperty("voice", voice.id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
