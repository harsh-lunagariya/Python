import threading
import time 
from concurrent.futures import ThreadPoolExecutor
def func(second):
    print(f"Sleeping for {second} second")
    time.sleep(second)
    return second

def main():
         
    # time1 = time.perf_counter()
    # func(4)
    # func(2)
    # func(1)
    # time2 = time.perf_counter()
    # print(time2 - time1)
        
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
        

    time1 = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()

    # t1 puru na thay tya sudhi t2 nai chalee 
    # without join directly apne count karsu to confilct that ane '0 ' second print thase

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time2 - time1)


def poolingdemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func,3)
        # future2 = executor.submit(func,4)
        # future3 = executor.submit(func,5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l =[3,4,5,6]
        results = executor.map(func,l)
        for result in results:
            print(result)
    

poolingdemo()









# from time import sleep
# from threading import *

# class Hello(Thread):
#     def run(self):
#         for i in range(12):
#             print("hello")
#             sleep(0.5)
        
# class Hi(Thread):
#     def run(self):
#         for i in range(12):
#             print("hi")
#             sleep(0.5)
           
# s1 = Hello()
# s2 = Hi()

# s1.start()
# sleep(0.2)
# s2.start()