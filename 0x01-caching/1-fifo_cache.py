#!/usr/bin/python3
'''
FIFO caching module'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        '''
        Get an item by key
        '''
        return self.cache_data.get(key, None)
