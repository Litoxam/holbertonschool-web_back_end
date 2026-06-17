#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Execute wait_random n times at the same time and return the delays."""
    tasks = []
    # Create a list of n tasks
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delay_list = []
    # Stocks the delays in a list and sort them asc
    delay_list = await asyncio.gather(*tasks)
    delay_list.sort()

    return delay_list

if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
