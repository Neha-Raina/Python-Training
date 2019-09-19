from threading import Thread
from time import sleep

class Mythread(Thread):
    

    def run(self):
        print("Thread started....",self.getName())
        sleep(3)
        print("Thread Finished.........",self.getName())

# ______________________________________

t1 = Mythread()
t1.start()
t2 =Mythread()
t2.start()
Thread.join(t1)
Thread.join(t2)
print("_________Done______")