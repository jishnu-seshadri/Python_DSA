#converts decimal number to the base of any other no.

from pythonds.basic import Stack

def converter(dec_num, base):
    
    rem_stack = Stack()
    
    while dec_num > 0:
        
        rem = dec_num % base
        rem_stack.push(rem)
        dec_num = dec_num // base
    
    new_str = ""
    
    while not rem_stack.isEmpty():
        new_str += str(rem_stack.pop())
    
    return new_str
        
print(converter(256, 16))
            
        
    