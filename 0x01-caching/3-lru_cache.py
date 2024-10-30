#!/usr/bin/python3
'''
LRU caching module'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''
    BaseCache inherits from BaseCaching and implements caching functionality
    '''
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Add an item in the cache
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_recently_use, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_recently_use)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''
        Get an item by key
        '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
