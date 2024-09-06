#!/usr/bin/env python3
"""
LFUCache - Least Frequent Used cache
"""
from base_caching import BaseCaching
from collections import deque


class LFUCache(BaseCaching):
    """
    LFUCache class - Least Frequent Used Cache
    """

    def __init__(self):
        super().__init__()
        self.key_list = dict()
        self.key_list_lru = deque([])

    def put(self, key, item):
        """add element
        """
        if not key or not item:
            return None

        self.cache_data[key] = item

        if key not in self.key_list.keys():
            self.key_list[key] = 0
        else:
            self.key_list[key] += 1
        self.key_list = dict(sorted(self.key_list.items(),
                             key=lambda item: item[1]))

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            dict_iterator = iter(self.key_list)
            least_frequent_used = next(dict_iterator)

            duplicate = False
            chk_duplicate = []
            for k in dict_iterator:
                if self.key_list[k] == self.key_list[least_frequent_used]:
                    duplicate = True
                    if least_frequent_used not in chk_duplicate:
                        chk_duplicate.append(least_frequent_used)
                    chk_duplicate.append(k)

            if not duplicate:
                del (self.cache_data[least_frequent_used])
                print('DISCARD {}'.format(least_frequent_used))
                del (self.key_list[least_frequent_used])
            else:
                for element in self.key_list_lru:
                    if element in chk_duplicate:
                        del (self.cache_data[element])
                        print('DISCARD {}'.format(element))
                        del (self.key_list[element])
                        self.key_list_lru.remove(element)
                        break

        if key not in self.key_list_lru:
            self.key_list_lru.append(key)
        else:
            self.key_list_lru.remove(key)
            self.key_list_lru.append(key)
        # print("from put {}".format(self.key_list))
        # print("from put {}".format(self.key_list_lru))

    def get(self, key):
        """Get element
        """
        if not key:
            return None
        item = self.cache_data.get(key)
        if item:
            self.key_list[key] += 1
            self.key_list_lru.remove(key)
            self.key_list_lru.append(key)
        self.key_list = dict(sorted(self.key_list.items(),
                                    key=lambda item: item[1]))
        # print("from get {}".format(self.key_list))
        # print("from get {}".format(self.key_list_lru))
        return item
