import pytube
import ffmpeg
dir="./data/"
dir_aud=dir+"audio/"
dir_vid=dir+"video/"
video_format=".mp4"
audio_format=".mp3"      


def download_highest_quality(url_link):
    yt= pytube.YouTube(url_link,use_oauth=False)
    yt.streams.filter(progressive=False).order_by(attribute_name="resolution").desc().first().download(dir_vid,filename=yt.title + video_format)
    yt.streams.get_audio_only().download(dir_aud,filename=yt.title + audio_format)
    print("download fertig")
    video = ffmpeg.input(dir_vid+yt.title+video_format).video
    audio = ffmpeg.input(dir_aud+yt.title+audio_format).audio
    ffmpeg.concat(video,audio,v=1,a=1).output(dir+yt.title+video_format).run()


def download_mp3(url_link):
    yt= pytube.YouTube(url_link,use_oauth=False)
    yt.streams.get_audio_only().download(dir,filename=yt.title+audio_format)
    print("download fertig")
