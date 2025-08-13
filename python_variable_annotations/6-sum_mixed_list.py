#!/usr/bin/env python3
"""Module for function that finds the sum of a mixed list."""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list."""
    return sum(mxd_lst)
