def shell_sort(a_list):
    
    n = len(a_list)
    gap = n // 2
    
    while gap>0:
        
        for start_pos in range(gap):
            
            j = start_pos + gap  
            
            while j < n:
                if a_list[j] < a_list[j-gap]:
                    a_list[j], a_list[j-gap] = a_list[j-gap], a_list[j]
                j += gap
            print(a_list)
        gap = gap//2
                            

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)