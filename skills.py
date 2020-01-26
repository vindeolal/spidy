'''
New skills can be added to my_skills dictionary.
Key should be a string that will be present is the command.
Value for each key must be an array of two element where first element is the response
from spidy and second element is a python file which contains action for that command.
File receives original command as its argument and will get executed for that command.
'''

my_skills = {
    'who are you': ['My name is spidy, I am your personal assistant', None],
    'your name': ['My name is spidy, I am your personal assistant', None],
    'open website': [None, "openWebsite.py"],
    'play song': [None, "playSong.py"]
}
