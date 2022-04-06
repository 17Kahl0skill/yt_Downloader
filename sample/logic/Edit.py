import ffmpeg


# alles bezüglich ffmpeg und wie die Files geedited werden müssen
def combine_2_mp4(name,dir_vid,dir_aud):
    video = ffmpeg.input(dir_vid+name+".mp4").video
    audio = ffmpeg.input(dir_aud+name+".mp3").audio
    ffmpeg.concat(video,audio,v=1,a=1).output("./data"+name+".mp4").run()
    return True
