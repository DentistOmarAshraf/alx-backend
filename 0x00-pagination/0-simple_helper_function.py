#!/usr/bin/env python3
"""
index_range - simple helper function
"""
from typing import Optional, Tuple


def index_range(page: int, page_size: int) -> Optional[Tuple[int, int]]:
    """
    page: 1-indexed page number
    page_size: number of items in one page
    return: tuple of start and end indexes of page
    """
    if page <= 0:
        return None
    return ((page - 1) * page_size, page * page_size)
