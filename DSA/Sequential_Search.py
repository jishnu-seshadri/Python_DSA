"""
Sequential Search - unordered
"""

def SeqSearch(a_list, item):
    pos = 0
    found = False
    for i in range(len(a_list)):
        if a_list[i] == item:
            found = True 
            return True
    return found


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(SeqSearch(test_list, 3))
print(SeqSearch(test_list, 13))
