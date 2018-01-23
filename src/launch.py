try:
    import pyttsx3 as pyttsx
    from lib.python.common import notify
    speak = pyttsx.init()
except:
    pass
import webbrowser


def execute(text):
    try:
        speak.say("opening "+text)
        speak.runAndWait()
        webbrowser.open('http://www.'+text+'.com')
    except:
        print('Sorry Mr.Rohan,unable to access it. Cannot hack either-IMF protocol!')
