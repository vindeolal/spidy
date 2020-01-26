import sys

import speech_recognition

from skills import my_skills
from speechToText import listener
from textToSpeech import text_to_speech

recognizer = speech_recognition.Recognizer()
microPhone = speech_recognition.Microphone()


def spidy(command):
    for key in my_skills:
        if key in command:
            reply, action = my_skills[key]
            sys.argv = [command]
            if action:
                exec(open(f'./{action}').read())
            if reply:
                text_to_speech(reply)
            else:
                pass


with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=5)
    text_to_speech('Ready for command')
    while True:
        speech = listener(recognizer, source)
        if speech:
            spidy(speech)
        else:
            print('could not listen you')
            continue
