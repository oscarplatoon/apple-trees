from apple import Apple
class AppleTree:
    apples = []
    appleTreeAgeToHaveApple = 3
    appleTreeLifeSpan = 100
    def __init__(self):
        self.age = 0
        self.height = 0
        self.alive = True
    def age_tree(self):
        self.age += 1
        self.height += 1
        for x in range(self.age, self.appleTreeLifeSpan):
            self.apples.append(Apple(10))           
        print(self.apples)
    def is_dead(self):
        if self.age > self.appleTreeLifeSpan:
            self.alive = True
        else:
            self.alive = False
        return self.alive        

    def any_apples(self):
        if len(self.apples) > -1:
            return True
        else:
            return False

    def pick_an_apple(self):
        raise Exception('No apples on your tree')
    
        # Read the tests before coding.
