import time
import asyncio

s = time.time()

async def fatch_file():
    print('Start fatching')
    await asyncio.sleep(1)
    print('File Fatch completely')

async def main():
    print('Start main')
    await asyncio.gather(fatch_file(),    # gather() execute all the corouting concurrently no need to create task
    fatch_file(),
    fatch_file())
    
    print('Complete main')

asyncio.run(main())

e=time.time()

print(e-s)

# Handling of file - aiofiles
# aiohttp - use for fatching images over internet