class Node:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if self.cache.get(key):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.remove(self.cache[key])
            del self.cache[key]

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.next
            prev, nxt = self.left, node.next
            prev.next = nxt
            nxt.prev = prev
            del self.cache[node.key]
