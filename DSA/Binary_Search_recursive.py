"""
Binary Search - recursive
"""

def rec_BinSearch(a_list, item):
    
    if len(a_list)==0:      #terminating condn
        return False
    
    first = 0
    last = len(a_list)-1
    
    midpt = int((first+last)//2)
    if a_list[midpt] == item:
        return True
    elif a_list[midpt] < item:
        return rec_BinSearch(a_list[midpt+1:], item)
    else:
        return rec_BinSearch(a_list[:midpt-1], item)
        

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(rec_BinSearch(test_list, 3))
print(rec_BinSearch(test_list, 13))
        