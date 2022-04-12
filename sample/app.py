import logic.Downloader as Download


def main():
    link = "https://www.youtube.com/playlist?list=PLiFoS88a9gul5peVkX39uRC_BkuR7-QqH"
    # Download.download_mp3("https://www.youtube.com/watch?v=2BCHVVj9AH4")
    downl = Download.Downloader()

    # downl.download_playlist(link)
    downl.download_playlist(link)
    downl.download_playlist(
                            "https://www.youtube.com/watch?v=-GJPhGWyg9E&list=PLkt97dAk8QOCvdZOMSOClVeHG0S64dKA1")
    downl.download_mp3("https://www.youtube.com/watch?v=uEznHztDoK4&list=RDGMEM6ijAnFTG9nX1G-kbWBUCJAVMLfIZcvxpFR8&index=2")
    return


if __name__ == "__main__":
    main()
