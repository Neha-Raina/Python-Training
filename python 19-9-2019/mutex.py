from time import sleep
from threading import Thread
from threading import Lock

class Resource:

    def __init__(self,lock):
        self.lock = lock

    def doTask(self):
        self.lock.acquire()
        print("Writing started........")
        sleep(3)
        print("Writing Finished.........")
        self.lock.release()
# --------------------------------------------------
class ResourceThread(Thread):

    def __init__(self,r):
        Thread.__init__(self)
        self.res = r

    def run(self):
        self.res.doTask()

# ----------------------------
lock = Lock()
res = Resource(lock)
t1 = ResourceThread(res)
t2 = ResourceThread(res)
t1.start()
t2.start()