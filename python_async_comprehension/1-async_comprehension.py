#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result

if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
