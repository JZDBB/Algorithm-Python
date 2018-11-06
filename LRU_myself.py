
import random
MEMORY = {}

class LRU():
    def __init__(self, capacity):
        self.cache = {}
        self.list_cache = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.list_cache.remove(key)
            list_tem = self.list_cache
            self.list_cache = [key]
            self.list_cache.extend(list_tem)
            return [key, self.cache[key]]

        else:
            if key in MEMORY:
                self.cache[key] = MEMORY[key]
                list_tem = self.list_cache
                self.list_cache = [key]
                self.list_cache.extend(list_tem)
                if len(self.list_cache) > self.capacity:
                    rm_key = self.list_cache[self.capacity]
                    self.list_cache.remove(rm_key)
                    del self.cache[rm_key]
                return  [key, MEMORY[key]]
            else:
                return None

    def set(self, key, value):
        if key in MEMORY:
            print("Username is exist!")
            return
        else:
            self.cache[key] = value
            list_tem = self.list_cache
            self.list_cache = [key]
            self.list_cache.extend(list_tem)
            MEMORY[key] = value
            if len(self.list_cache) > self.capacity:
                rm_key = self.list_cache[self.capacity]
                self.list_cache.remove(rm_key)
                del self.cache[rm_key]
            print("Username added!")

if __name__ == '__main__':

    cache = LRU(6)

    for i in range(10):
        cache.set(i, i)

    for i in range(10):
        num = random.randint(1, 10)
        print(cache.get(num))
    print(MEMORY)
    print(cache.list_cache)

