#!/usr/bin/python3
'''
LIFO caching module'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
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
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
        

    def get(self, key):
        '''
        Get an item by key
        '''
        return self.cache_data.get(key, None)
