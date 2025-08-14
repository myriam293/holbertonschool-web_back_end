#!/usr/bin/env python3
"""Module for task_wait_n function."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> 
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of delays in the order they were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
