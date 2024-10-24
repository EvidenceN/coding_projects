import asyncio

async def task_1():
    print("Task 1 running")
    await asyncio.sleep(1)
    print("Task 1 complete")

async def task_2():
    print("Task 2 running")
    await asyncio.sleep(2)
    print("Task 2 complete")

async def main():
    t1 = asyncio.create_task(task_1())
    t2 = asyncio.create_task(task_2())
    
    # Wait until both tasks are completed
    await t1
    await t2

asyncio.run(main())
