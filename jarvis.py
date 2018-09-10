# coding: utf-8
from gui import MyFrame
from scripts.actions import events,notify
import pyttsx3 as pyttsx
import speech_recognition as sr
import threading
import ctypes
import os
import notify2
# import asyncio
# import uvloop
import subprocess
from scripts import req
from multiprocessing import Process
import functools

headers = {'''user-agent':'Chrome/53.0.2785.143'''}
#speak=wicl.Dispatch("SAPI.SpVoice")

speak = pyttsx.init()

#async def utlisCheck(check):

def cont(text=None):
	if text:
		events(text[1],text[2:])
	else:
		r=sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio=r.listen(source)

		try:
			x = r.recognize_google(audio)
			print(x)
			x=x.lower()
			link=x.split()
			if check.Fuck_internetCheck is 0:
				threading.Thread(target=req(x)).start()
			else:
				threading.Thread(target=events(x,link)).start()

		except:
			notify("Sorry Boss, Try again!")
			cont()

if __name__=="__main__":
#	check = ctypes.CDLL(os.path.dirname(os.path.realpath(__file__))+'/lib/cpp/libint.so')
#	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
#	loop=asyncio.get_event_loop()
#	for signame in ('SIGINT','SIGTERM'):
#		loop.add_signal_handler(getattr(signal,signame),lambda: asyncio.ensure_future(ask_exit(signame)))
	while True:
		r=sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source,duration=1)
			print("Say Something")
			audio=r.listen(source)

		try:
			x = r.recognize_google(audio)
			x=x.lower()
			threading.Thread(target=req(x)).start()
		except:
			print("No audio detected")
'''
	try:
		print("Running")
		loop.run_forever()
	finally:
		loop.close()

if x=="jarvis" and first is 0:
	speak.say("Yes Boss")
	speak.runAndWait()
	x=x.split()
	text=x[1:]
	first=first+1
	cont()
else:
	threading.Thread(target=req(x)).start()
'''
