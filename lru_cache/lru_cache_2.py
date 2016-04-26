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

    def promote(self, node):
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

    def add_key(self, key_node):
        self.keys.add_front(key_node)
        self.size += 1

    def promote(self, key_node):
        self.keys.promote(key_node)

    def prune(self):
        self.size -= 1
        return self.keys.del_tail()

    def get(self, key):
        """
        :rtype: int
        """
        try:
            val, key_node  = self.cache[key]
            self.promote(key_node)
            return val
        except Exception as e:
            print type(e)
            print e.args
            print e
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cache.has_key(key):
            key_node = self.cache[key][1]
            self.cache[key] = (value, key_node)
            self.promote(key_node)
            return
        if self.size ==  self.capacity:
            del self.cache[self.prune()]
        node = LinkedNode(key)
        self.cache[key] = (value, node)
        self.add_key(node)


c = LRUCache(2)
print c.get(3)
#c.set(2,1)
#c.set(1,1)
#c.set(2,3)
#c.set(4,1)
#print 'get1'
#print 'ret=' ,c.get(1)
#print 'get2'
#print 'ret=',c.get(2)
