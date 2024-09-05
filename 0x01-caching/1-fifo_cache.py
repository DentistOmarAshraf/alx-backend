#!/usr/bin/env python3
"""
FIFOCache - class of cache based on FIFO algorithm
to discard items
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    FIFOCache - first in first out
    """

    def __init__(self):
        super().__init__()
        self.key_list = deque([])

    def put(self, key, item):
        """add item to parent class dict
        """
        if not key or not item:
            return None
        self.cache_data[key] = item

        if key not in self.key_list:
            self.key_list.append(key)
        else:
            self.key_list.remove(key)
            self.key_list.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_element_key = self.key_list.popleft()
            del (self.cache_data[first_element_key])
            print('DISCARD: {}'.format(first_element_key))

    def get(self, key, item):
        """get element from parent dict
        """
        if not key:
            return None
        return self.cache_data.get(key)
