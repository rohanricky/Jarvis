'''
    Opens GUI directly
'''
import tkinter as tk
from tkinter import ttk
import pyttsx3 as pyttsx
from scripts.actions import events
import speech_recognition as sr
import threading
import ctypes
import subprocess
import os
from scripts import req
from src.sync import execute
from multiprocessing import Process
from scripts.tasks import tasks

#A stdout class to redirect output to tkinter window
class StdRedirector(object):

	def __init__(self, text_window):
		self.text_window = text_window

	def write(self, output):
		self.text_window.insert(tk.END, output)

class MyFrame(tk.Frame):
        def __init__(self,*args,**kwargs):
            tk.Frame.__init__(self,*args,**kwargs)
            self.textBox = tk.Text(root,
			height=1,width=30,
			font=("Times", 16),
			bg="#666", fg="#0f0",
			spacing1=6, spacing3=6,
			insertbackground="#0f0"
            )
#            self.textBox = tk.Text(root,height=1,width=50)
#            self.textBox.insert("1.0", "$>")
            self.textBox.grid(row=1,column=1, padx=10, pady=10)
            #self.grid(padx=10,pady=10)
            root.bind('<Return>', self.OnEnter)
            self.textBox.focus_set()
#            self.audioInput=''
            self.say('''Hello Sir, A pleasure to see you work''')
            self.photo1 = tk.PhotoImage(file="images/mic_icon.png")
            self.btn = ttk.Button(root,command=self.OnClicked,
            image=self.photo1, style="C.TButton")
            self.btn.grid(row=1,column=2, padx=10, pady=20)

        def printf(self):
            print("Fuck You")

        def say(self, arg):
            engine = pyttsx.init()
            engine.say(arg)
            engine.runAndWait()

        def OnClicked(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.textBox.delete('1.0',tk.END)
                self.say('Listening Boss')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                print("Recognizing audio...")
                put=r.recognize_google(audio)
                print(put)
                self.textBox.insert('1.0',put)
                put=put.lower()
                link=put.split()
                threading.Thread(target=events(put,link)).start()
                self.textBox.delete('1.0',tk.END)
            except sr.UnknownValueError:
                logging.info("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logging.info("Could not request results from Google Speech Recognition service; {0}".format(e))

        def OnEnter(self,event=None):
            put=self.textBox.get("1.0","end-1c")
            self.textBox.delete("1.0",tk.END)
            print(put)
            put=put.lower()
            link = put.split()
            threading.Thread(target=req(put)).start()
#            p=Process(target=events,args=(put,link)).start()
# multiprocessing is Overloading the processors
# Implement queue based threading

    #Trigger the GUI. Light the fuse!
if __name__=="__main__":
    check = ctypes.CDLL(os.path.dirname(os.path.realpath(__file__))+'/lib/cpp/libint.so')
    root = tk.Tk()
    view = MyFrame(root)
    style=ttk.Style()
    style.configure('C.TButton',
        background='#555',
        highlightthickness='0'
	)
    style.map("C.TButton",
		background=[('pressed', '!disabled', '#333'), ('active', '#666')]
    )
    print('Opening GUI')
    root.title("Jarvis")
#    Process(target=tasks).start()
#        threading.Thread(target=sync("yoyo")).start()
#    root.geometry('{}x{}'.format(400, 100))
    root.configure(background="#444")
#    view.pack(side="top",fill="both",expand=False)
    root.mainloop()
