#!/usr/bin/env python3
"""Least frequently used caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """class for least frequently used caching system.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, _key):
        """Order items in cached based on the most recently used item.
        """
        max_index = []
        freq = 0
        pos = 0
        ins = 0
        for i, freq_key in enumerate(self.keys_freq):
            if freq_key[0] == _key:
                freq = freq_key[1] + 1
                pos = i
                break
            elif len(max_index) == 0:
                max_index.append(i)
            elif freq_key[1] < self.keys_freq[max_index[-1]][1]:
                max_index.append(i)
        max_index.reverse()
        for pos in max_index:
            if self.keys_freq[pos][1] > freq:
                break
            ins = pos
        self.keys_freq.pop(pos)
        self.keys_freq.insert(ins, [_key, freq])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, freq_key in enumerate(self.keys_freq):
                if freq_key[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
