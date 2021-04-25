# -*- coding: utf-8 -*-
"""
Self defined class Queue
"""
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def ADD(self, item):
        self.items.insert(0, item)
    
    def REM(self):
        self.items.pop()
        
    def disp(self):
        print(self.items)
        
q = Queue()
q.ADD(5)
q.ADD('dog')
q.ADD('yaay')
q.REM()

q.disp()

c = [i for i in range(1,10,3)]
q.ADD(c)
q.disp()

q.ADD(42)
q.disp()
