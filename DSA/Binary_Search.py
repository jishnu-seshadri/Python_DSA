"""
Binary Search
"""

def BinSearch(a_list, item):
    
    first = 0
    last = len(a_list)-1
    found = False
    
    while not found and first <= last:
        midpt = int((first+last)//2)
        if a_list[midpt] == item:
            found = True
        elif a_list[midpt] < item:
            first = midpt + 1
        else:
            last = midpt - 1
        
    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BinSearch(test_list, 3))
print(BinSearch(test_list, 13))
        