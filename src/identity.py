try:
    import pyttsx3 as pyttsx
    from lib.python.common import notify
    speak = pyttsx.init()
except:
    pass
from templates.text import TextTemplate

def execute(text):
    try:
        speak.say("I am Jarvis, Mr Rohan's Assistant")
        speak.runAndWait()
        notify("I am Jarvis, Mr Rohan's Assistant")

    except:
        print('Error. Try reading the ReadMe to know about me!')
