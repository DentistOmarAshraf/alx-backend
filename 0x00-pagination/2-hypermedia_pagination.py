#!/usr/bin/env python3
"""
Class Server
"""
import csv
import math
from typing import List


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
        """Get Page dataset
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        start: int = (page - 1) * page_size
        end: int = page * page_size
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get Hyper
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)
        prev_page = page - 1
        next_page = page + 1

        dict_to_ret = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page if next_page < total_pages else None,
            'prev_page': prev_page if prev_page > 0 else None,
            'total_pages': total_pages
        }

        return dict_to_ret
