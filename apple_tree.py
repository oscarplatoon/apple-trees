from apple import Apple

class AppleTree:
    def __init__(self):
        self.age = 0
        self.height = 0
        self.apple_count = []

    def age_tree(self):
        self.age += 1
        if self.height <= 300:
            self.height += 10
        if self.age >= 4:
            new_apple = Apple(self.age)
            self.apple_count.append(new_apple)
   
    def is_dead(self):
        if self.age < 100:
            return False
        return True
    
    def any_apples(self):
        if len(self.apple_count) > 0:
            return True
        else:
            return False

    def pick_an_apple(self):
        if self.any_apples():
            return self.apple_count.pop()
        raise Exception('No apples on your tree')

