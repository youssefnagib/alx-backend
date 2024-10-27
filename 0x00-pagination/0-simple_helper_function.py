#!/usr/bin/env python3
'''
This model calculates the start
and end indices for a given page and page size.
'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    this function returns the index range for a given page
    and page size
    Args:
        page (int): the current page number
        page_size (int): the number of items per page

    Returns:
        tuple: a tuple containing the start
        and end indices for the current page
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
