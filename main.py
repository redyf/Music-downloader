from pytube import YouTube


def downloadAudio(VIDEO_URL):
    convert_url_to_string = str(VIDEO_URL)


    yt = YouTube(convert_url_to_string)

    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()


downloadAudio()

