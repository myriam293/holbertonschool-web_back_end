#!/usr/bin/env python3
"""Measure the average runtime per execution of wait_n."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return the average time.

    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average runtime per execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
