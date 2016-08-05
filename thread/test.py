import threading
import asyncio

async def hello():
    print('1')
    await asyncio.sleep(1)
    print('2')

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()