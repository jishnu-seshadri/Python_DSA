import random

class Dice:
    
    def __init__(self, no_sides):
        self.num_sides = no_sides
        self.roll()
    
    def roll(self):
        self.current_val = random.randrange(1,self.num_sides+1)
        return self.current_val
    
my_val = Dice(6)
for i in range(10):
    print(my_val.roll())
    
    
    
            
    
        