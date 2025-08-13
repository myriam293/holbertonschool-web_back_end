#!/usr/bin/env python3
"""Module for function that creates a tuple with a string and the square of a number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and the second is v squared as a float."""
    return k, float(v ** 2)
