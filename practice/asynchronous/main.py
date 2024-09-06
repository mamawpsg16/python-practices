import asyncio

# EXAMPLE  1 
# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)
#     print("Data fetched!")
#     return "Some data"

# async def main():
#     result = await fetch_data()
#     print(result)

# The asyncio.run() function to run the top-level entry point “main()” function

# asyncio.run(main()) 
# asyncio.run(main = main())

import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def nested():
    return 42

async def main():
    #EXAMPLE 2

    #     print(f"started at {time.strftime('%X')}")

    #     await say_after(1, 'hello')
    #     await say_after(2, 'world')

    #     print(f"finished at {time.strftime('%X')}")

    #EXAMPLE 3

    # # 1 second faster to use create_task
    # task1 = asyncio.create_task(
    #     say_after(1, 'hello'))

    # task2 = asyncio.create_task(
    #     say_after(2, 'world'))

    # print(f"started at {time.strftime('%X')}")

    # # Wait until both tasks are completed (should take
    # # around 2 seconds.)
    # await task1
    # await task2

    # print(f"finished at {time.strftime('%X')}")

    # EXAMPLE 4 
    
    # async with asyncio.TaskGroup() as tg:
    #     tg.create_task(
    #         say_after(1, 'hello'))

    #     tg.create_task(
    #         say_after(2, 'world'))

    #     print(f"started at {time.strftime('%X')}")

    # # The await is implicit when the context manager exits.

    # print(f"finished at {time.strftime('%X')}")

    # AWAITABLES
    # nested() # ERROR need to use await
    # Let's do it differently now and await it:
    # print(await nested())  # will print "42".

    # TASKS
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)

asyncio.run(main())