
from curses import window
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from pytube import YouTube
import os
from kivy.uix.widget import Widget
Window.size = (500, 500)
#set the window title
Window.title = "JULIAN UI TES"
out_dir = "YT-Downloads"

class Downloader(MDApp, Widget):
    
    Window.title = "JULIAN UI TEST"
    def build(self):
        kv = Builder.load_file("styles.kv")
        return kv
    


    def downloadV(self, link):
        try:
            link = link.text
            yt = YouTube(link)
            try:
                os.rename(f'{out_dir}/{title}.mp4', f'{out_dir}/{title}(old).mp4')
            except:
                print("No old file")
            yt.streams.get_highest_resolution().download(out_dir)
            title = yt.title
        except:
            pass
    def downloadA(self, link):
        try:
            link = link.text
            yt = YouTube(link)
            title = yt.title
            title = title.replace(",", "")
            title = title.replace(".", "")
            title = title.replace('"', "")
            title = title.replace("|", "")  
            title = title.replace("/", "")
            title = title.replace("\\", "")
            title = title.replace("?", "")
            title = title.replace(">", "")
            title = title.replace("<", "")
            title = title.replace("*", "")
            title = title.replace(":", "")
            yt.streams.get_audio_only().download(out_dir)
            os.rename(f'{out_dir}/{title}.mp4', f'{out_dir}/{title}.mp3')
            

        except:
            pass
Downloader().run()