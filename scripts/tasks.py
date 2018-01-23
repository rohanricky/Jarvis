# When system is idle perform these tasks. 30 seconds

import subprocess
import ctypes
from src.sync import execute
import os
path=os.path.dirname(os.path.realpath(__file__))
pardir=os.path.join(path,os.pardir)
check = ctypes.CDLL(pardir+'/lib/cpp/libint.so')

def tasks():
    print(check.Fuck_phoneCheck)
    if check.Fuck_phoneCheck is 0:
        execute()

    #Careful with Trash it may permanently delete important files
    subprocess.call('rm -r /home/rohan/.local/share/Trash/files/*',shell=True)
    subprocess.call('rm -r /home/rohan/.local/share/Trash/info/*',shell=True)

# Run time taking programs & machine learning algos here
if __name__=='__main__':
    tasks()
