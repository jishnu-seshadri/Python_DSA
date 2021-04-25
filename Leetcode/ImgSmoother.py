import math

def imageSmoother(M):
    
    rows = len(M)
    cols = len(M[0])
    
    ans = [[0 for y in range(cols)] for x in range(rows)] 
    
    kernal = [[0.125 for x in range(3)] for y in range(3)] 
    
    for c in range(cols):
        for r in range(rows):
            
            sum = 0
            count = 0
            
            for i in (r-1, r, r+1):
                for j in (c-1, c, c+1):
                    if(i>= 0 and i <=rows-1 and j <=cols-1 and j>=0):
                        sum += M[i][j]
                        count += 1
            
            ans[r][c] = math.floor(sum/count)
    return ans

imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])