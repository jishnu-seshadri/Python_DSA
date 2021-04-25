class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:   
    def __init__(self):
        self.head = None
      
    def isEmpty(self):
        return self.head == None
        # if self.head == None:
        #     return True

    def add(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def find(self, data):
        current = self.head
        found  = False
        while not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found
    
    def remove(self, data):
        current = self.head
        previous = None
        found  = False
        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous == None:
                self.head = current.next
            else:
                previous.next = current.next
    
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


l1 = LinkedList()
for i in range(1, 19, 2):
    l1.add(i)
    #print('added: ',i)

l1.printList()

            
