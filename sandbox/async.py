#!/usr/bin/python
import asyncio
import time

todo = ["get package", "laundry", "bake cake"]

delay_s = 1


async def do_work(work):
    print(f"'{work}' Started ")
    await asyncio.sleep(delay_s)
    print(f"'{work}' Completed")
    return {"work": work}


async def main():
    start = time.perf_counter()
    responses = await asyncio.gather(*[do_work(work) for work in todo])
    for response in responses:
        print(response)
    end = time.perf_counter()
    print(f"It took : {end - start:.2f} seconds")


if __name__ == '__main__':
    # main()
    asyncio.run(main())
