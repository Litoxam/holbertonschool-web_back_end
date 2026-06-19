#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute four async comprehensions in parallel and return the runtime."""
    start = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    async def main():
        return await (measure_runtime())

    print(
        asyncio.run(main())
    )
