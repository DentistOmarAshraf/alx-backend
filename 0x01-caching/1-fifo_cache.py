#!/usr/bin/env python3
"""FIFOCache - class of cache based on FIFO algorithm
to discard items
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache - first in first out
    """

    def put(self, key, item):
        """add item to parent class dict
        """
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        if len(self.cache_data) == 4:
            first_element_key = next(iter(self.cache_data))
            del (self.cache_data[first_element_key])
            print('DISCARD: {}'.format(first_element_key))
        self.cache_data[key] = item

    def get(self, key, item):
        """get element from parent dict
        """
        if not key:
            return
        return self.cache_data[key]
