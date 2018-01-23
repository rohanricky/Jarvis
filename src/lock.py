import subprocess

try:
    import pyttsx3 as pyttsx
    from lib.python.common import notify
    speak = pyttsx.init()
except:
    pass

def execute(text):
    try:
        speak.say("locking the device")
        speak.runAndWait()
        notify("locking the device")
        subprocess.run("xdg-screensaver lock",shell=True,check=True)
    except :
        print('Cannot lock device')
