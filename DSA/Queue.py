"""
Queue

can do as a list also

can do from other direction also
Instead of:
    insert --> append
    pop() --> pop(0)
"""
class Queue:
    
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
