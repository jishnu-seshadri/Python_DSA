class Solution:
    
    def reverse(self, x: int) -> int:
        digits = ''
        
        isNegative = True if x < 0 else False
        
        if isNegative:
            x = -x
        
        while x > 0:
            rem = x%10
            digits = digits + str(rem)
            x = x//10

        n = -int(float(digits)) if isNegative else int(float(digits))
        
        return n