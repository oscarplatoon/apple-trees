import random
from apple import Apple

class AppleTree:
    def __init__(self):
        self.height = 0   
        self.age = 0
        self.production_age = random.randint(4,8)
        self.growth_stop = random.randint(40,60)
        self.apple_number  = 0
  
    def age_tree(self):
        self.age += 1
        if(self.age < self.growth_stop):
            self.height += random.randint(5,10)/10
        if(self.age >= self.production_age):
            self.apple_number += (1000 * (self.age/100)*(random.randint(50,100)/100))
        
   
    def is_dead(self):
        if self.age >= 100:
            return True
        else:
            return False
    
    def any_apples(self):
        if self.apple_number > 0:
            return True
        else:
            return False
        

    def pick_an_apple(self):
        if self.apple_number == 0:
            raise Exception('No apples on your tree')
        else:
            self.apple_number -= 1
            return(Apple())
        # Read the tests before coding.
