#!/usr/bin/env python3
"""Module for executing multiple wait_random coroutines concurrently."""



async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay.
    Return list of delays in ascending order without using sort().
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)
    return delays
