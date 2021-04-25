
"""
Selection_sort

"""

def selSort(a_list):
    
    for last_pos in range(len(a_list)-1, 0, -1):
        pos_max = 0        
        for i in range(last_pos+1):
            if a_list[i] > a_list[pos_max]:
                pos_max = i
                
        temp = a_list[last_pos]
        a_list[last_pos] = a_list[pos_max]
        a_list[pos_max] = temp
        
        print(a_list, "pass {} over".format(len(a_list)-last_pos))
        
                 
a_list = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
selSort(a_list)

