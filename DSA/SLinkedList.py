class Node:
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        current = Node(item)
        current.next = self.head
        self.head = current
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.next
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found    
            
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:     #breaks if one after last node is reached
                break    
            if current.data == item:
                found = True          
            else:
                previous = current
                current = current.next
        
        if previous == None:    #element in 1st pos
            self.head = current.next         
        
        elif found:
            previous.next = current.next
        else:
            print('Element not found')
            
    def printlist(self):
        current = self.head
        while current:
            print(current.data)
            #print('\t')
            current = current.next
 

ll = LinkedList()
ll.add(3)
ll.add(5)
ll.add(7)
ll.add(9)

ll.printlist()

ll.remove(10)
ll.printlist()

            