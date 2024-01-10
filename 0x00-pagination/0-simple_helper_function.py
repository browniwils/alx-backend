#!/usr/bin/env python3

"""Module for a simple pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Creates paginationg with start and size of page.
    """
    if isinstance(page, int) and isinstance(page_size, int):
        return ((page - 1) * page_size, page_size * page)
    raise TypeError('Expected `page` and `page_size` to be ints')
