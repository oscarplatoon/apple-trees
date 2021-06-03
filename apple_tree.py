from apple import Apple

class AppleTree:
    def __init__(self):
        self.height = 0
        self.age = 0
        self.dead = False
        self.apples = []
        
    def age_tree(self):
        if self.dead == False:
            self.age += 1
            if self.age < 30:
                self.height += 1
            self.apples.append(Apple(15))
            if self.age > 100:
                self.dead = True

    def is_dead(self):
        if self.age > 100:
            self.dead = True
        return self.dead
    
    def any_apples(self):
        if (len(self.apples) > 0):
            return True
        return False
            

    def pick_an_apple(self):
        try:
            picked_apple = self.apples.pop()
        except:
            raise Exception('No apples on your tree')
        return picked_apple
        # Read the tests before coding.
