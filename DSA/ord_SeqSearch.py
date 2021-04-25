"""
Sequential Search - ordered
"""

def ord_SeqSearch(a_list, item):
    pos = 0
    found = False
    for i in range(len(a_list)):
        if a_list[i] == item:
            found = True 
            return True, i
        elif item <  a_list[i]:
            return False
    return found


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ord_SeqSearch(test_list, 3))
print(ord_SeqSearch(test_list, 13))