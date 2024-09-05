#!/usr/bin/env python3
"""
BasicCache Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inheret BaseCaching
       - where data is saved in classe
    """

    def put(self, key, item):
        """add item to parent class
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get item from parent class
        """
        if not key:
            return None
        return self.cache_data.get(key)
