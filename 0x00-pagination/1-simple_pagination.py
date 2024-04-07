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
