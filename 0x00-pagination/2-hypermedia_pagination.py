#!/usr/bin/env python3

"""
This module demonstrates simple pagination
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    This function returns a tuple containing a start index and an end
    index corresponding to the range of indexes to return a list for
    those particular pagination parameters
    """
    end_index = page * page_size
    if page == 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size
    return (start_index, end_index)


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
        """
        This function paginates a dataset and returns the appropriate
        page of the dataset(i.e. the correct list of rows)
        """
        if type(page) is not int:
            assert type(page) is int, AssertionError
        if type(page_size) is not int:
            assert type(page_size) is int, AssertionError
        if page <= 0:
            assert page > 0, AssertionError
        if page_size <= 0:
            assert page_size > 0, AssertionError
        dataset = self.dataset()
        index = index_range(page, page_size)
        if index[1] < len(dataset):
            page_list = [dataset[i] for i in range(index[0], index[1])]
        else:
            page_list = []
        return page_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This function returns a dictionary containing the following
        key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        parsed_data = self.dataset()

        if ((len(parsed_data) - 1) % page_size) == 0:
            total_pages = math.trunc((len(parsed_data) - 1) / page_size)
        else:
            total_pages = math.trunc(((len(parsed_data) - 1) / page_size) + 1)
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
