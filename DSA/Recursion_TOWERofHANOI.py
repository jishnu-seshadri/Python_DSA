"""
Recursion_TOWERofHANOI
"""


def Tower(num, f, aux, to):                # number, from, to, aux
    
    if num>0:
        Tower(num-1, f, to, aux)
        print("Move disc {} from {} to {}".format(num,f,to))
        global count
        count += 1
        Tower(num-1, aux, f, to)          
            
count = 0
Tower(3, 'A', 'B', 'C')                            # A-from, B-to, C-Aux
print(count)