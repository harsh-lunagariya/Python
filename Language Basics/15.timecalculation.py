import time

s = time.time()
i=0
for _ in range(100000):
    i+=1
e = time.time()

print(f"time is {e-s:.8f} second {i}")