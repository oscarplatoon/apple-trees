class AppleTree:
    def __init__(self, height):
        self.height = height
  
    def age_tree(self, age):
        self.age = age + 1
   
    def is_dead(self, age):
        if self.age >= 100:
            self.age = True
    
    def any_apples(self):
        pass

    def pick_an_apple(self):
        raise Exception('No apples on your tree')
        # Read the tests before coding.
