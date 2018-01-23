try:
    import notify2
    found=True
except:
    pass
from queue import PriorityQueue

notify2.init('Jarvis')
q=PriorityQueue(maxsize=0)

def notify(summary,message=''):
    if found is True:
        n = notify2.Notification(summary,message)
        n.set_timeout(1000)
        n.show()

def taskQueue(text):
    q.put(text)
    if q.empty():
        print("Empty")

taskQueue("H")
