import time
import asyncio

s = time.time()

async def get_ticket():
    await asyncio.sleep(0.0002)
    print('got ticket')

async def like_ig():
    await asyncio.sleep(0.0004)
    print('got liked')

async def other():
    await asyncio.sleep(0.0001)
    print("other is done")

async def main():
    task1 = asyncio.create_task(get_ticket())
    task2 = asyncio.create_task(like_ig())
    task3 = asyncio.create_task(other())

    
    await task1
    await task2
    await task3


asyncio.run(main())
e = time.time()

print(e-s)