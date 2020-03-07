### Spidy is a personal assistant written in python.

### Existing skills
> who are you

> open website "website name"

> play "video name" (will play the video from YouTube)


### To add new skills
New skills can be added to `my_skills` dictionary. Key should be a string that will be present is the command you speek and value 
for each key must be an array of two element where first element is the response from spidy and second element is a python file
which contains action for that command. File receives original command as its argument and will get executed for that command.
