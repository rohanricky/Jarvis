import subprocess
import asyncio
import os
#from lib.python.common import notify

def execute(text=None):
	new_songs= os.environ['HOME']+"/Music/new/"
	x=subprocess.Popen("ls /run/user/*/gvfs",stdout=subprocess.PIPE,shell=True)
	filename=x.communicate()[0]
	filename=filename.decode()
	filename=filename.strip()
	print(filename)
	if os.listdir(new_songs):
		print("/run/user/1000/gvfs/"+filename+"/Internal\ storage/Music")
		subprocess.run("cp "+os.environ['HOME']+"/Music/new/* "+os.environ['HOME']+"/Music",shell=True)
		subprocess.run("mv "+os.environ['HOME']+"/Music/new/* /run/user/1000/gvfs/"+filename+"/Internal\ storage/Music",shell=True,check=True)

	else:
		print("No new songs")
