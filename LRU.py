# coding: utf-8
from collections import OrderedDict
import random


class LRUCache(OrderedDict):
    def __init__(self, size=5):
        self.size = size,
        self.cache = OrderedDict()

    def get(self, key):
        if self.cache.has_key(key):
            val = self.cache.pop(key)
            self.cache[key] = val
        else:
            val = None

        return val

    def set(self, key, val):
        if self.cache.has_key(key):
            val = self.cache.pop(key)
            self.cache[key] = val
        else:
            if len(self.cache) == self.size:
                self.cache.popitem(last=False)
                self.cache[key] = val
            else:
                self.cache[key] = val


if __name__ == '__main__':
    """ test """
    cache = LRUCache(6)

    for i in range(10):
        cache.set(i, i)

    for i in range(10):
        i = random.randint(1, 20)
        print('cache', cache.cache.keys())
        if cache.get(i):
            print('hit, %s\n' % i)
        else:
            print('not hit, %s\n' % i)


