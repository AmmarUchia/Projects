from ctypes import resize
import imp
from select import select
import moviepy


from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube   

#functions
def select_path():
    #allows user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def Download_file():
    #get user path 
    get_link = Link_f.get()
    #get selected path
    user_path = path_label.cget('text')
    #Download Video Function
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()    
    vid_clip= VideoFileClip(mp4_video)
    vid_clip.close()
screen = Tk()
Title = screen.title('Youtube Downloader')
canvas = Canvas(screen,width=500 , height= 500)
canvas.pack()
#image Logo
Logo_img = PhotoImage(file='yt.png')
#resize
Logo_img = Logo_img.subsample(2,2)
canvas.create_image(250,80,image=Logo_img)
#Link Field
Link_f = Entry(screen,width=50)
link_label = Label(screen,text='Enter Link: ',font=('Arial',15))
#select path
path_label = Label(screen,text="Select Path For Download",font=('Arial',15))
select_btn= Button(screen,text="Select",command=select_path)
#Add To Window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

#Add Widgets
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=Link_f)
#Download Buttons
download_buttons = Button(screen,text='Download File',command=Download_file)
#add to canvas
canvas.create_window(250,390,window=download_buttons)

screen.mainloop()