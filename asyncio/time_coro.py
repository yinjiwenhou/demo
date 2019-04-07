import time
import asyncio

async def hello():
    print('Hello world. %s' % time.ctime())
    await asyncio.sleep(1)
    print('Hello again. %s' % time.ctime())

loop = asyncio.get_event_loop()
task = loop.create_task(hello())
print(task)
loop.run_until_complete(task)
print(task)
loop.close()
