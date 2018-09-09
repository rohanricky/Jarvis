'''
This file is called when your device is offline only

GoTo src/* for online assistant replies
'''
# coding: utf-8
import re
import os
from urllib.request import urlopen
import wikipedia
import time
import webbrowser
import json
import requests
import ctypes
import urllib
import ssl
from bs4 import BeautifulSoup
import logging
import speech_recognition as sr
import sqlite3
import subprocess
import threading
import youtube_dl
import asyncio

try:
    import pyttsx3 as pyttsx
    import notify2
    import tkinter as tk
    found=True
except:
    pass

 ## Use asyncio module to avoid blockages
requests.packages.urllib3.disable_warnings()

try:
        _create_unverified_https_context=ssl._create_unverified_context
except 'AttributeError':
        pass
else:
        ssl._create_default_https_context=_create_unverified_https_context

try:
    speak = pyttsx.init()
except:
    pass

def notify(summary,message=''):
    if found is True:
        notify2.init('Jarvis')
        n = notify2.Notification(summary,message)
        n.set_timeout(1000)
        n.show()

def events(put,link):
    identity_keywords = ["who are you", "who r u", "what is your name"]
    youtube_keywords = ("play", "stream", "queue")
    launch_keywords = ("open", "launch")
    search_keywords = ("search", "google")
    wikipedia_keywords = ("wikipedia", "wiki")
    search_pc = ("find","lookfor")
    todo = ('remind')
    download_music=("download","dude","z")
    shutdown=("shutdown","shut down")
    print(link)

    if put.startswith(download_music):
        link = '+'.join(link[1:])
        print(link)
        say = link.replace('+', ' ')
        url = 'https://www.youtube.com/results?search_query='+link
#                 webbrowser.open('https://www.youtube.com'+link)
        fhand=urlopen(url).read()
        soup = BeautifulSoup(fhand, "html.parser")
        songs = soup.findAll('div', {'class': 'yt-lockup-video'})
        hit = songs[0].find('a')['href']
#                   print(hit)
#        speak.say("downloading "+say)
#        speak.runAndWait()
        notify("Downloading "+say)
        ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'mp3',
                                            'preferredquality': '192',
                                            }],
                                            'quiet': True,
                                            'restrictfilenames': True,
                                            'outtmpl': os.environ['HOME']+'/Music/%(title)s.%(ext)s'
                                            }

        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download(['https://www.youtube.com'+hit])
        notify("Song Download Complete")

    elif put.startswith(youtube_keywords):
        try:
            link = '+'.join(link[1:])
            say = link.replace('+', ' ')
            url = 'https://www.youtube.com/results?search_query='+link
#                    webbrowser.open('https://www.youtube.com'+link)
            fhand=urlopen(url).read()
            soup = BeautifulSoup(fhand, "html.parser")
            songs = soup.findAll('div', {'class': 'yt-lockup-video'})
            hit = songs[0].find('a')['href']
#                    print(hit)
            speak.say("playing "+say)
            speak.runAndWait()
            webbrowser.open('https://www.youtube.com'+hit)
        except:
            print('Sorry Rohan. Looks like its not working!')

    elif any(word in put for word in identity_keywords):
        try:
            speak.say("I am Jarvis, Mr Rohan's Assistant")
            speak.runAndWait()
            notify("I am Jarvis, Mr Rohan's Assistant")

        except:
            print('Error. Try reading the ReadMe to know about me!')
#Open a webpage
    elif put.startswith(launch_keywords):
                try:
#                    print(link[1])
                    speak.say("opening "+link[1])
                    speak.runAndWait()
                    webbrowser.open('http://www.'+link[1]+'.com')
                    print("Hi")
                except:
                    print('Sorry Mr.Rohan,unable to access it. Cannot hack either-IMF protocol!')
        #Google search
    elif put.startswith(search_keywords):
                try:
                    link='+'.join(link[1:])
                    say=link.replace('+',' ')
                    notify("searching google for "+say)
                    webbrowser.open('https://www.google.com/search?q='+link)
                except:
                    print('Nope, this is not working.')
        #Wikipedia
    elif put.startswith(wikipedia_keywords):
                try:
                    link = '+'.join(link[1:])
                    say = link.replace('+', ' ')
                    wikisearch = wikipedia.page(say)
                    notify("Opening wikipedia page for" + say)
                    webbrowser.open(wikisearch.url)
                except:
                    print('Wikipedia could not either find the article or your Third-world connection is unstable')
       #Lock the device
    elif put.startswith('secure'):
        try:
            speak.say("locking the device")
            speak.runAndWait()
            notify("locking the device")
#            ctypes.windll.user32.LockWorkStation()
            subprocess.run("xdg-screensaver lock",shell=True,check=True)
        except :
            print('Cannot lock device')

    elif put.startswith('hello'):
#        asyncio.create_subprocess_shell("python3 gui.py")  Redirect output
        subprocess.run("python3 gui.py",shell=True,check=True)

    elif put.startswith('push'):
        try:
            repo=link[1]
            message=link[2]
            if repo and message:
                subprocess.run(put,shell=True,check=True)
        except:
            print("Couldn't push")

    elif put.startswith(search_pc):
        process=subprocess.Popen("find $HOME -name "+link[1],shell=True,stdout=subprocess.PIPE)
        stdout=process.communicate()[0]
        notify(stdout)
        found=stdout.decode()
        print(found)
        try:
            subprocess.run("xdg-open "+found,shell=True,check=True)
        except:
            speak.say("Sorry,couldn't open")
    elif put.startswith(shutdown):
        subprocess.run("shutdown -h now",shell=True,check=True)

'''
    elif put.startswith('sync'):
        notify("Syncing songs")
        execute()
#delete execute later
'''
'''
this short script erases all the data from the connected smartphone. I haven't tried it yet
    elif put.startswith("hack"):
        x=subprocess.Popen("ls /run/user/*/gvfs",stdout=subprocess.PIPE,shell=True)
    	filename=x.communicate()[0]
    	filename=filename.decode()
    	filename=filename.strip()
    	print(filename)
    	print("/run/user/1000/gvfs/"+filename+"/Internal\ storage/Music")
    	subprocess.run("rm -rf /run/user/1000/gvfs/"+filename+"/Internal\ storage/*",shell=True,check=True)
'''
