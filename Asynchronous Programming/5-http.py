# Asynchronous http request with multythreading
import requests
import time
import aiohttp 
import asyncio
from threading import *

# s = time.time()

# for i in range(1,151):
#     url = 'https://pokeapi.co/api/v2/pokemon/'+str(i)
#     resp = requests.get(url)
#     pokemon = resp.json()
#     print(pokemon['name'])

# e = time.time()


# print(e-s)

# 23.9709575176239

# s = time.time()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         for i in range(1,151):
#             url = 'https://pokeapi.co/api/v2/pokemon/'+str(i)
#             async with session.get(url) as resp:
#                 pokemon = await resp.json()
#                 print(pokemon['name'])

# asyncio.run(main())

# e = time.time()


# print(e-s)

# 6.096141815185547

s = time.time()

class th1(Thread):
    def run(self):
        async def main():
            async with aiohttp.ClientSession() as session:
                for i in range(1,51):
                    url = 'https://pokeapi.co/api/v2/pokemon/'+str(i)
                    async with session.get(url) as resp:
                        pokemon = await resp.json()
                        print(pokemon['name'])  
        asyncio.run(main())
class th2(Thread):
    def run(self):
        async def main():
            async with aiohttp.ClientSession() as session:
                for i in range(51,101):
                    url = 'https://pokeapi.co/api/v2/pokemon/'+str(i)
                    async with session.get(url) as resp:
                        pokemon = await resp.json()
                        print(pokemon['name'])  
        asyncio.run(main())
class th3(Thread):
    def run(self):
        async def main():
            async with aiohttp.ClientSession() as session:
                for i in range(101,151):
                    url = 'https://pokeapi.co/api/v2/pokemon/'+str(i)
                    async with session.get(url) as resp:
                        pokemon = await resp.json()
                        print(pokemon['name'])  
        asyncio.run(main())

t1 = th1()
t2 = th2()
t3 = th3()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

e = time.time()


print(e-s)