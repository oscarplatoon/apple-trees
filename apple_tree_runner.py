from apple_tree import AppleTree

tree = AppleTree()

while tree.any_apples() == False:
    tree.age_tree()

print(f"My apple tree is producing apples at age {tree.age} and is {tree.height} feet tall")

while tree.is_dead() == False: 
    apple_basket = []

    while tree.any_apples(): 
        apple_basket.append(tree.pick_an_apple())

    avg_diameter = 0
    for x in apple_basket:
        avg_diameter += x.diameter
    avg_diameter= avg_diameter/len(apple_basket)

    

    print(f"Year {tree.age} Report")
    print(f"Tree height: {round(tree.height,2)} feet")
    print(f"Harvest:     {len(apple_basket)} apples with an average diameter of {round(avg_diameter,2)} inches")

    # Age the tree another year
    tree.age_tree()

print(f"The tree is now dead at age {tree.age}! Time to plant a new one!")
