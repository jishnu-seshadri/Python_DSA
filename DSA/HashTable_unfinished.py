"""
Hash Table  Implementation

One list, called slots, will hold the key items and a parallel list, called data, will hold
the data values.


"""
class HashTable:
    def __init__(self):
        self.size = 11                  #prime no to avoid coliision
        self.slots = [None]*self.size   #keys
        self.data = [None]*self.size    #values
        
    def put(self, key, data):
        