import subprocess
try:
    from lib.python.common import notify
except:
    pass
import os

def execute(text):
    process=subprocess.Popen("find $HOME -name "+text,shell=True,stdout=subprocess.PIPE)
    stdout=process.communicate()[0]
    notify(stdout)
    found=stdout.decode()
    print(found)
    try:
        subprocess.run("xdg-open "+found,shell=True,check=True)
    except:
        print("Sorry,couldn't open")
