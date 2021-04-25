"""
Insertion_sort

"""

def insertionSort(a_list):
        
    for pos in range(1, len(a_list)):
        
        index = pos
        value_to_be_sorted = a_list[pos]
        
        while index > 0 and value_to_be_sorted < a_list[index-1]:
            a_list[index] = a_list[index-1]
            index -= 1
        
        a_list[index] = value_to_be_sorted
        print(a_list, "pass {} over".format(pos))

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print("\nfinal answer:", alist)