#!/usr/bin/env python3
"""
MRUCache - Most Recent Used
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class saving cached memo according MRU
    """

    def __init__(self):
        super().__init__()
        self.key_list = list()

    def put(self, key, item):
        """add new element to parent class dict
        """
        if not key or not item:
            return None
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recent_element = self.key_list.pop()
            del (self.cache_data[most_recent_element])
            print('DISCARD: {}'.format(most_recent_element))

        if key not in self.key_list:
            self.key_list.append(key)
        else:
            self.key_list.remove(key)
            self.key_list.append(key)

    def get(self, key):
        """get element
        """
        if not key:
            return None
        item = self.cache_data.get(key)
        if item:
            self.key_list.remove(key)
            self.key_list.append(key)
        return item
