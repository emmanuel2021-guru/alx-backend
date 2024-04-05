#!/usr/bin/python3

"""
This module contains a function that returns a tuple of size two
containing a start index and an end index corresponding to the range of
indexes to return a list for those particular pagination parameters
"""


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
