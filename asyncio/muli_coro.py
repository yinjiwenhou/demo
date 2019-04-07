import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('Woring: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coro_1 = do_some_work(1)
coro_2 = do_some_work(2)
coro_3 = do_some_work(3)

tasks = [
    asyncio.ensure_future(coro_1),
    asyncio.ensure_future(coro_2),
    asyncio.ensure_future(coro_3),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task result:', task.result())

print('Time: ', now() - start)