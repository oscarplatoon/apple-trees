from apple import *
class AppleTree:

    def __init__(self, height, age):
       self.height = height
       self.age = age
  
    def age_tree(self):
        self.age += 1
        self.height += 1
        
   
    def is_dead(self):
        if self.age >= 100:
            return True
        else:
            return False
    
    def any_apples(self):
        if self.age < 10:
            return False
        else:
            return True


    def pick_an_apple(self):
        if self.any_apples():
            raise Exception('No apples on your tree')
        else:
            return Apple()
        # Read the tests before coding.