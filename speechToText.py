import speech_recognition


# https://www.codesofinterest.com/2017/03/python-speech-recognition-pocketsphinx.html
def listener(recognizer, source):
    print('listening..')
    speech = recognizer.listen(source)
    try:
        print('converting to text..')
        text = recognizer.recognize_google(speech).lower()
        print('listener, ' + text)
        return text

    except speech_recognition.UnknownValueError:
        print('unable to process speech')
        pass
