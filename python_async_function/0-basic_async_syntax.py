#!/usr/bin/env python3
"""Module for an asynchronous coroutine that waits a random delay."""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds and return it."""
    wait_time = random.uniform(0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time