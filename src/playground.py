import asyncio

class Looper:

    def __init__(self):
        self.a = 1
        self.b = 2
        pass

    async def run(self):
        # while True:
        #     self.a += 1
        #     self.b += 1
        #     await asyncio.sleep(0.00001)
        while True:
            self.a += 1
            if (self.a % 3 == 0):
                print(self.a)
        return self.a

async def go():
    l = Looper()
    asyncio.create_task(l.run())
    while True:
        pass
        # runner = l.run()
        # await runner
        # print(l.a)

# asyncio.run(go())

# loop = asyncio.get_event_loop()
# l = Looper()
# loop.create_task(l.run())
# loop.run_forever()
# while True:
#     print(687)

async def taco():
    print(687)

async def potato():
    await taco()
    print(1678)

asyncio.run(potato())

