# import pool_otherhtml,more_img
# import threading
# import asyncio
#
# loop = asyncio.get_event_loop()
# # tasks = [pool_otherhtml.main(),more_img.main()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
import threading
import asyncio
from multiprocessing import Pool

async def hello():
    print('1')
    print('2')

async def print1():
    print(input('enter'))

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),print1(),print1()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

