class Node:

    def __init__(self, key=None, value=None, prevNode=None, nextNode=None):
        self.key = key
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.nextNode = self.right
        self.right.prevNode = self.left

    def prioritize(self, key):
        # delete it
        curr = self.cache[key]
        curr.nextNode.prevNode = curr.prevNode
        curr.prevNode.nextNode = curr.nextNode

        # place before "right"
        curr.nextNode = self.right
        curr.prevNode = self.right.prevNode
        curr.prevNode.nextNode = curr
        self.right.prevNode = curr
    
    def remove(self):
        del self.cache[self.left.nextNode.key]
        self.left.nextNode = self.left.nextNode.nextNode
        self.left.nextNode.prevNode = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.prioritize(key)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val == -1:
            if (len(self.cache) == self.capacity):
                self.remove()
            # add at end
            add = Node(key=key, value=value)
            add.nextNode = self.right
            add.prevNode = self.right.prevNode
            add.prevNode.nextNode = add
            self.right.prevNode = add
            self.cache[key] = add
        else:
            self.prioritize(key)
            self.cache[key].value = value

