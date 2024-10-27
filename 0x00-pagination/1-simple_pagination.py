#!/usr/bin/env python3
'''
This model calculates the start
and end indices for a given page and page size.
'''


from typing import Tuple
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_index, end_index = index_range(page, page_size)
        if end_index > len(self.dataset()):
            end_index = len(self.dataset()) - 1
        if start_index > end_index:
            return []
        return self.dataset()[start_index:end_index]
