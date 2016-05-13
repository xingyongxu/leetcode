from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()


    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val
        return -1


c = LRUCache(2)
print c.get(3)
c.set(2,1)
c.set(1,1)
c.set(2,3)
c.set(4,1)
print 'get1'
print 'ret=' ,c.get(1)
print 'get2'
print 'ret=',c.get(2)


