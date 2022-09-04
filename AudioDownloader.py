from email.mime import audio
from youtube_dl import YoutubeDL
audio_down= YoutubeDL({'format':
'bestaudio'})   
while True:
    try:
        print('Youtube Downloader'.center(45,'_'))
        Url = input("Enter Youtube Url: ")
        audio_down.extract_info(Url)
    except  Exception:
        print("Couldnt \'t  Download The Audio")
    finally:
        option = int(input('\n1.Downoad again\n.Exit\n\nOption Here: '))

        if option != 1:
            break                