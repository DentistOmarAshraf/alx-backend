#!/usr/bin/env python3
"""
LIFOCache class - Last In First Out
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class save cahch according to LIFO algo
    """

    def __init__(self):
        super().__init__()
        self.key_list = list()

    def put(self, key, item):
        """add item to parent class dict
        """
        if not key or not item:
            return None
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_element_key = self.key_list.pop()
            del (self.cache_data[last_element_key])
            print('DISCARD: {}'.format(last_element_key))

        if key not in self.key_list:
            self.key_list.append(key)
        else:
            self.key_list.remove(key)
            self.key_list.append(key)

    def get(self, key):
        if not key:
            return None
        return self.cache_data.get(key)
