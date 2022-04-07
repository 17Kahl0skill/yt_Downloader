import logic.Downloader as Download


def main():
    link = "https://www.youtube.com/playlist?list=PLiFoS88a9gul5peVkX39uRC_BkuR7-QqH"
    # Download.download_mp3("https://www.youtube.com/watch?v=2BCHVVj9AH4")
    downl = Download.Downloader()

    # downl.download_playlist(link)
    downl.download_playlist(link)
    downl.download_playlist("https://www.youtube.com/watch?v=iPwNeM9I1-M&list=OLAK5uy_mojkYya3VWhN4f1CNlg8urMNhYBfwrUeE")
    downl.download_playlist("https://www.youtube.com/watch?v=Eg84Eu_Qonw&list=OLAK5uy_kUu4FarXr48s_uQqrEpwCE-uOobKic5xQ")
    downl.download_playlist("https://www.youtube.com/watch?v=XRP9k9nlAfE&list=PLMEOLAYxGgstLEUGRx8kCF15EFBG5M95X&index=1")
    downl.download_playlist("https://www.youtube.com/watch?v=inHbha2nyPs&list=PLMEOLAYxGgsttujEl1yBrKAdUsVBcX7U3")
    del downl
    return


if __name__ == "__main__":
    main()
