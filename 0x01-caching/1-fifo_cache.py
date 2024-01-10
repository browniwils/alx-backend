#!/usr/bin/env python3
"""FIFO caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """class for FIFO caching system.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            _key, _val = self.cache_data.popitem(False)
            print("DISCARD:", _key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
