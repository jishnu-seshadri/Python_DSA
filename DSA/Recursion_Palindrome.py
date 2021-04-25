"""
Recursion_Palindrome

"""
def Palin(s):
    def toChar(s):                  #converts to lower and only char
        s = s.lower()
        ans = ''
        for character in s:
           if character in 'abcdefghijklmnopqrstuvwxyz':
               ans = ans + character
            
        return ans

    def isPal(s):               
        if len(s) < 2: 
            return True
        else:                       #checks first==last and returns rest slice
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChar(s))


    

