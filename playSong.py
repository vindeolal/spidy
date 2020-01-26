import re
import sys

import pafy
import vlc

from textToSpeech import text_to_speech

# make sure vlc player is installed in the system use sudo apt-get install vlc for ubuntu
import urllib.request
from bs4 import BeautifulSoup

textToSearch = re.search('play song (.*)', sys.argv[0])
if textToSearch:
    query = urllib.parse.quote(textToSearch.group(1))
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    song_to_play = ''
    text_to_speech('searching song on youtube')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        if 'watch?v=' in vid['href']:
            song_to_play = vid['href']
            break
        else:
            continue
    if song_to_play:
        print(f'song url, https://www.youtube.com{song_to_play}')
        video_url = pafy.new(f'https://www.youtube.com{song_to_play}')
        best = video_url.getbest()
        text_to_speech(f"playing song {textToSearch.group(1)}")
        vlc_instance = vlc.Instance()
        vlc_player = vlc_instance.media_player_new()
        video = vlc_instance.media_new(best.url)
        video.get_mrl()
        vlc_player.set_media(video)
        vlc_player.play()
    else:
        print('no song found with matching string')
        text_to_speech('no song found')
        pass
else:
    pass
