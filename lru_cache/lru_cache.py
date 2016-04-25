class LinkedNode(object):
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LinkedList(object):
    def __init__(self):
        self.head = LinkedNode(None)
        self.tail = LinkedNode(None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        node.nxt = self.head.nxt
        self.head.nxt.prev = node
        node.prev = self.head
        self.head.nxt = node

    def del_tail(self):
        try:
            node = self.tail.prev
            node.prev.nxt = self.tail
            self.tail.prev = node.prev
            node.prev = None
            node.nxt = None
            return node.val
        except:
            return -1

    def promote(self, key):
        node = self.head.nxt
        if node.val == key:
            return
        while node != self.tail:
            if node.val == key: 
                break
            node = node.nxt
        if node !=  self.tail:
            p = node.prev
            n = node.nxt
            p.nxt = n
            n.prev = p
            self.add_front(node)

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.keys = LinkedList() 
        self.size = 0

    def add_key(self, key):
        self.keys.add_front(LinkedNode(key))
        self.size += 1

    def promote(self, key):
        self.keys.promote(key)

    def prune(self):
        self.size -= 1
        return self.keys.del_tail()

    def get(self, key):
        """
        :rtype: int
        """
        try:
            val = self.cache[key]
            self.promote(key)
            return val
        except Exception as e:
            print type(e)
            print e.args
            print e

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cache.has_key(key):
            self.cache[key] = value
            return
        if self.size ==  self.capacity:
            del self.cache[self.prune()]
        self.cache[key] = value
        self.add_key(key)


c = LRUCache(1)
c.set(2,1)
print c.get(2)
