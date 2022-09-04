from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)
video = yt.streams.get_highest_resolution
video.download()