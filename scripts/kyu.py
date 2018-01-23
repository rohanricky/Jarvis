import queue
import multiprocessing
from multiprocessing import Process
from . import req

cores = multiprocessing.cpu_count()
print(cores)

queue=queue.Queue()

def MyMightyQueue(item=None):
    if item.startswith("download"):
        queue.put_nowait(item)
    else:
        queue.put(item)
    

def worker():
    item=queue.get()
    if item is not None:
        break
    print(item)
    queue.task_done()
