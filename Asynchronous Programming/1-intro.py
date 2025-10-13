# it simpley mean coperative function that work in co-operative manner
# it doesn't block any other function execution while running

import asyncio

async def a():      # this give coroutine object
    print('cbiwf')

# To execute coroutine function you need to create an event loop
# asyncio.run automatically create this event loop

asyncio.run(a()) 

# Creating own evet loop

loop = asyncio.new_event_loop()

# define task
task1 = asyncio.sleep(2)

# execute task
loop.run_until_complete(task1)

# report message
print('Done')

# async is use to create coroutine and await is use to pause the coroutine

async def square(num):
    return num*num

async def main():
    x = await square(5)
    print(x)

    y = await square(10)
    print(y)

    Z = x+y
    print(Z)

asyncio.run(main())