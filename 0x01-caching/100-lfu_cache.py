#!/usr/bin/python3
'''
LFU caching module'''
from base_caching import BaseCaching
from collections import OrderedDict, Counter


class LFUCache(BaseCaching):
    '''
    LFUCache inherits from BaseCaching and implements caching functionality
    '''
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = Counter()

    def update_LFU(self, key):
        """Updates the frequency of the given key."""
        if key is not None:
            self.frequency[key] += 1

    def least_frequency_used(self):
        """Returns the least frequently used keys."""
        if not self.frequency:
            return []
        min_frequency = min(self.frequency.values())
        return [k for k, v in self.frequency.items() if v == min_frequency]

    def put(self, key, item):
        '''
        Add an item in the cache
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_LFU(key)
            self.cache_data.move_to_end(key, last=True)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_keys = self.least_frequency_used()
            lfu_key = min_keys[0]
            self.cache_data.pop(lfu_key)
            self.frequency.pop(lfu_key)
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item
        self.update_LFU(key)
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''
        Get an item by key
        '''
        if key is not None and key in self.cache_data:
            self.update_LFU(key)
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        return None
