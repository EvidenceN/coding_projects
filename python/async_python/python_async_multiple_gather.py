import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(2)
    print("Hello again after 2 seconds!")

async def say_goodbye():
    print("Goodbye!")
    await asyncio.sleep(1)
    print("Goodbye again after 1 second!")

async def main():
    await asyncio.gather(say_hello(), say_goodbye())

asyncio.run(main())
