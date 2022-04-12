import os
import pytube
import ffmpeg
import shutil


class Downloader():
    def __init__(self,
                 dir="data",
                 dir_aud="audio",
                 dir_vid="video",
                 format_video=".mp4",
                 format_audio=".mp3"):
        self.__dir = "./"+dir+"/"
        self.__dir_aud = self.__dir+dir_aud+"/"
        self.__dir_vid = self.__dir+dir_vid+"/"
        self.__format_video = format_video
        self.__format_audio = format_audio

    def download_playlist(self, url_link, is_mp3=True):
        pl = pytube.Playlist(url=url_link)
        __temp = self.__dir
        self.__dir = "./"+pl.title+"/"
        for vid in pl:
            print(vid)
            if is_mp3 is True:
                self.download_mp3(vid)
            else:
                self.download_highest_quality(vid)
        self.delete_temp_data()
        self.__dir = __temp

    def download_highest_quality(self, url_link):
        yt = pytube.YouTube(url_link, use_oauth=False)

        # video sortierung und download
        yt_vid = yt.streams.filter(progressive=False)
        yt_vid = yt_vid.order_by(attribute_name="resolution").desc()
        yt_vid = yt_vid.first().download(self.__dir_vid,
                                         filename=yt.title +
                                         self.__format_video)

        # audio sortierung und bester qualitäts download
        yt_aud = yt.streams.get_audio_only()
        yt_aud = yt_aud.download(self.__dir_aud,
                                 filename=yt.title + self.__format_audio)
        print("download fertig")

        # editing
        video = ffmpeg.input(self.__dir_vid+yt.title+self.__format_video).video
        audio = ffmpeg.input(self.__dir_aud+yt.title+self.__format_audio).audio
        edit = ffmpeg.concat(video, audio, v=1, a=1)
        edit.output(self.__dir+yt.title+self.__format_video).run()

    def download_mp3(self, url_link):
        yt = pytube.YouTube(url_link, use_oauth=False)
        yt.streams.get_audio_only().download(self.__dir,
                                             filename=yt.title +
                                             self.__format_audio)
        print("download fertig")

    def delete_temp_data(self):
        if os.path.exists(self.__dir_vid):
            shutil.rmtree(self.__dir_vid)
        if os.path.exists(self.__dir_aud):
            shutil.rmtree(self.__dir_aud)

    def __del__(self):
        self.delete_temp_data()
