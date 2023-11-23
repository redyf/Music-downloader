from pytube import YouTube

VIDEO_URL = "https://youtube.com/watch?v=QyiNcEPPb5o&feature=shared"
yt = YouTube(VIDEO_URL)


audio = yt.streams.filter(only_audio=True)[0]
audio.download()

