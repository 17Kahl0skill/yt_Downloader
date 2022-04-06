import ffmpeg

video = ffmpeg.input("./data/audio/test.mp4")
vid= ffmpeg.input("./data/vid/2.mp4")
audio = video.audio
vid2=vid.video
ffmpeg.concat(vid2,audio,v=1,a=1).output("./data/output/test2.mp4").run()