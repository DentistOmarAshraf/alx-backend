#!/usr/bin/env python3
"""
LRUCache - Least Recently used
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    class save caches according to LRU
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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used_element = self.key_list.popleft()
            del (self.cache_data[least_used_element])
            print('DISCARD: {}'.format(least_used_element))

        if key not in self.key_list:
            self.key_list.append(key)
        else:
            self.key_list.remove(key)
            self.key_list.append(key)

    def get(self, key):
        """get item from parent dict
        """
        if not key:
            return None
        item = self.cache_data.get(key)
        if item:
            self.key_list.remove(key)
            self.key_list.append(key)
        return item
