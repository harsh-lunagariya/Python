from time import sleep
from threading import *

# In multy threading you focus on workers 
# In Asyncronus programming focus on tasks

n=5

class Hello(Thread):
    def run(self):
        for i in range(n):
            print("Hello")
            sleep(0.05)

class Hi(Thread):
    def run(self):
        for i in range(n):
            print("Hi")
            sleep(0.05)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.02)
t2.start()

t1.join()
t2.join()

print("\nbye")


# this is diffrent way of creating a thread
def inf():
    while True:
        pass

def myname():
    print("this is kaxuckwb")

t1 = Thread(target=inf)
t2 = Thread(target=myname)

t1.start()
t2.start()