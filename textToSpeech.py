import os


def text_to_speech(text):
    """say converts text to audible speech using the GNUstep speech engine
    command to install: sudo apt-get install gnustep-gui-runtime"""
    print("textToSpeech, " + text)
    os.system('say ' + text)