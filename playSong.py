import pafy
import vlc

from textToSpeech import text_to_speech

# make sure vlc player is installed in the system use sudo apt-get install vlc for ubuntu
# TODO : make url dynamic based on song name/video name in the command

url = "https://www.youtube.com/watch?v=JGwWNGJdvx8"
video_url = pafy.new(url)
text_to_speech('playing song')
best = video_url.getbest()
vlc_instance = vlc.Instance()
vlc_player = vlc_instance.media_player_new()
video = vlc_instance.media_new(best.url)
video.get_mrl()
vlc_player.set_media(video)
vlc_player.play()
