
"""
Bubble_Sort_mod

efficienter version of bubble sort. Stops when no exchanges happen rather than
at the end of the list.
"""

def bubbleSort_mod(a_list):
    
    i= 0
    exchanges = True
    
    while i < (len(a_list)) and exchanges == True:
        
        exchanges = False        
        for j in range(len(a_list)-i-1):
            
            if a_list[j] > a_list[j+1]:
                
                 temp = a_list[j+1]         
                 a_list[j+1] = a_list[j]
                 a_list[j] = temp
                 exchanges = True 
                 
        if exchanges==True: 
            print(a_list)
        print("pass {} over".format(i+1))
        i += 1
                 
                 
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort_mod(a_list)
