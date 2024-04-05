#!/usr/bin/env python3

"""

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
        with open('Popular_Baby_Names.csv', newline='') as my_csv:
            parsed_data = list(csv.reader(my_csv, delimiter=','))
            index = index_range(page, page_size)
            csv_index = (index[0] + 1, index[1] + 1)
            new_list = []
            if (csv_index[1] < len(parsed_data)):
                for i in range(csv_index[0], csv_index[1]):
                    new_list.append(parsed_data[i])
            return new_list
