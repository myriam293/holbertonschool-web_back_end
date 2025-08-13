#!/usr/bin/env python3
"""Module for function that returns a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a
    float by the given multiplier."""
    def func(x: float) -> float:
        return x * multiplier
    return func
