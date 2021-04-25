
"""
Bubble_Sort

It compares adjacent items and exchanges those that are out of order. 
Each pass through the list places the next largest value in its proper place. 
In essence, each item “bubbles” to the back where it belongs.
"""

def bubbleSort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j+1]:
                 temp = a_list[j+1]         #swapping element and next elem 
                 a_list[j+1] = a_list[j]
                 a_list[j] = temp
            print(a_list)
        print("pass {} over".format(i+1))
                 
        #can also do swapping in python like this: a,b = b,a
                 
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(a_list)
