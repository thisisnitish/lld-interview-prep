# LLD/Machine Coding for LRU Cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, cap: int):
        self.capacity = cap
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # if the key is not present
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # self.remove_node(node) # No need of this line
        self.move_to_head(node)

        return node.val


    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = val

            self.move_to_head(node)

        else:
            node = Node(key=key, val=val)

            if len(self.cache) >= self.capacity:
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
            
            self.cache[key] = node
            self.add_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)

        return node
