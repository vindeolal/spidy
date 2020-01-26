import re
import sys
import webbrowser

from textToSpeech import text_to_speech

reg_ex = re.search('open website (.+)', sys.argv[0])
if reg_ex:
    domain = reg_ex.group(1)
    text_to_speech(f'opening website {domain}'.replace('.', ' dot '))
    webbrowser.open(f'https://www.{domain}')
else:
    pass
