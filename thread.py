from multiprocessing import Process,Queue,Pool,Pipe
import speech_recognition as sr
import pyttsx3 as pyttsx

speak = pyttsx.init()

def audio(conn2):
	while True:
		r=sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source,duration=1)
			print("Say Something")
			audio=r.listen(source)

		try:
			x = r.recognize_google(audio)
			x=x.lower()
			conn2.send(x)
			# print('1',queue.get())
		except:
			print("No audio detected")

def printQueue(x):
	print(x)

# queue = Queue()

# pool=Pool(processes=2)
# pool.map(audio, (queue,))

# if queue.get():
# 	pool.apply_async(printQueue)

conn1, conn2 = Pipe()
audioProcess = Process(target=audio, args=(conn2, ))
audioProcess.start()
mainProcess = Process(target=printQueue, args=(conn1.recv(),))
mainProcess.start()
audioProcess.join()
# audioProcess = Process(target=audio, args=(queue,))
# audioProcess.start()
# audioProcess.join(None)
# mainProcess = Process(target=printQueue)
# mainProcess.start()
# mainProcess.join()
# Process(target=req, args=(q.get(),))