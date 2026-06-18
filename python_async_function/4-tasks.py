#!/usr/bin/env python3
"""Execute multiple tasks concurrently and collect their results."""

import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create n tasks, execute them concurrently,
    and return their delays in ascending order."""
    tasks = []
    # Create a list of n tasks
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Stocks the delays in a list and sort them asc
    delay_list = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list

if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
