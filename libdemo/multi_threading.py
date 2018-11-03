
import threading

class PrintThread(threading.Thread):
    def run(self):
        print("In Child thread!")
        for i in range(1,21):
            print( self.getName(), "-> ", i)


print(threading.current_thread().getName())
t1 = PrintThread()
t1.setName("Child1")
t2 = PrintThread()
t2.setName("Child2")

t1.start()
t2.start()

