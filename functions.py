'''
Created on October 2, 2016

Matthew W
'''
import os
import shutil
import sys
import time

from urllib import request
import youtube_dl
import tkinter as tk
from tkinter import ttk


def download(url,bitrate,win):
    win.destroy()
    playlist = True
    bitrate = str(bitrate)
    ydl_opts = {
    'format': 'bestaudio/best', # choice of quality  
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': bitrate,
    }], # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'noplaylist' : playlist        # only download single song, not playlist
    }
    
    url = [url]
    print(url)
    programDirectory = os.getcwd()
    goToDownLoadFolder(programDirectory)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:   
        ydl.download(url)   
            

def goToDownLoadFolder(programDirectory):
    os.chdir(programDirectory)
    os.chdir("..")
    currentDirectory = os.getcwd()
    downloadsDirectory = currentDirectory + "\\Downloads"
    #checking for existance of database
    try:
        if(os.path.isdir(downloadsDirectory) == False):
            os.mkdir("Downloads")
            shutil.copy(programDirectory+"\\ffmpeg.exe", downloadsDirectory)
            shutil.copy(programDirectory+"\\ffprobe.exe", downloadsDirectory)
        else:
            if(os.path.isdir(downloadsDirectory+"\\ffmpeg.exe") == False ):
                shutil.copy(programDirectory+"\\ffmpeg.exe", downloadsDirectory)
            if(os.path.isdir(downloadsDirectory+"\\ffprobe.exe") == False ):
                shutil.copy(programDirectory+"\\ffprobe.exe", downloadsDirectory)
    except:
        print("ffmpeg or ffprobe not found in song downloader folder")
        time.sleep(100)
        sys.exit("_____closing script___")
    os.chdir(downloadsDirectory)

                                                                                           
                 
def cleanUpHTML(html):
    #gets rid of all the uninterperated html
    html = html.replace("\\n","")
    html = html.replace("\\xe2","")
    html = html.replace("\\x98","")
    html = html.replace("\\x99","")
    html = html.replace("\\x8b","")
    html = html.replace("\\x86","")
    html = html.replace("\\x8b","")
    html = html.replace("\\x86","")
    return html