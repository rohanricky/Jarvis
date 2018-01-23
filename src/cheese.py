import subprocess
import time

#Video recording
subprocess.run("ffmpeg -i /dev/video0 myvid.mp4",shell=True)

#Photo capture
subprocess.run("avconv -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:2 -frames 1 /tmp/out.jpg",shell=True)
