'''
miscellaneous short scripts which are not worth a separate file
'''

import wikipedia
import webbrowser
import subprocess
import os
import ctypes

try:
    from lib.python.common import notify
except:
    pass

#check = ctypes.CDLL(os.path.dirname(os.path.realpath(__file__))+'/lib/cpp/libint.so')

def execute(text):
    shutdown=('shutdown','shut down')
    wikipedia_keywords = ("wikipedia", "wiki")
    make_dir = ("make","create")
    if text.startswith(shutdown):
        subprocess.run("shutdown -h now",shell=True,check=True)

    elif text.startswith('hello'):
#        asyncio.create_subprocess_shell("python3 gui.py")  Redirect output
        subprocess.run("python3 gui.py",shell=True,check=True)

    elif text.startswith('push'):
        try:
            repo=link[1]
            message=link[2]
            if repo and message:
                subprocess.run(put,shell=True,check=True)
        except:
            print("Couldn't push")

    elif any(word in text for word in wikipedia_keywords):
        try:
            wikisearch = wikipedia.page(text)
            notify("Opening wikipedia page for" + text)
            webbrowser.open(wikisearch.url)
        except:
            print("Wikipedia not stable")

    elif any(word in text for word in make_dir):
        link=text.split()
        os.chdir('/home/rohan/github')
        os.mkdir(link[1],mode=0o777)

    elif text.startswith('tests'):
        link=text.split()
        os.chdir('/home/rohan/tests')
        open(link[1],'a')

    elif text.startswith('wifi'):
        link = text.split()
        if link[1]=="off" or link[1]=="disable":
            notify('You have an internet connection already')
            os.system("nmcli radio wifi off")

        elif link[1]=="on" or link[1]=="enable":
            os.system("nmcli radio wifi on")
