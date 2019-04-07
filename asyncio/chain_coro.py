import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('Wating: ', x)
    await asyncio.sleep(x)
    return('Done after {}s'.format(x))

async def main():
    coro_1 = do_some_work(1)
    coro_2 = do_some_work(2)
    coro_3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(coro_1),
        asyncio.ensure_future(coro_2),
        asyncio.ensure_future(coro_3),
    ]

    # dones, pending = await asyncio.wait(tasks)
    # dones = await asyncio.gather(*tasks)
    dones = asyncio.as_completed(tasks)

    for task in dones:
        result = await task
        print('Task result: ', result)

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('Time: ', now() - start)