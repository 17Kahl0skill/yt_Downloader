import pytube
import ffmpeg

def main():
    yt= pytube.YouTube("https://www.youtube.com/watch?v=JkgwxUpfTZ4",use_oauth=False)
    # yt.streams.filter(only_video=True,adaptive=True).first().download()
    vid=yt.streams.filter(progressive=False).order_by(attribute_name="resolution").desc().first().download("./data/vid/")
    name= yt.title
    audio=yt.streams.get_audio_only().download("./data/audio/")
    

    print(name)
    print("download fertig")
    vid=ffmpeg.input("./data/vid/"+name+".mp4")
    audio=ffmpeg.input("./data/audio/"+name+".mp4")
    test= ffmpeg.output(audio.audio,"./data/audio/test.mp3")
    ffmpeg.run(test)
    #ffmpeg.concat(audio,vid,v=1,a=1).output("./data/test").run()
    #ffmpeg.concat(vid,audio,v=1,a=1).output("./data/output/test.mp4").run()

if __name__ == "__main__":
    main()