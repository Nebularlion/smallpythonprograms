import random

def throw(dice_amount, dice_sides, roll_amount):
    results = []
    for roll in range(roll_amount):
        for dice in range(dice_amount):
            result = random.randint(1, dice_sides)
            results.append(result)
    return results

dice_amount = int(input("How many dices do you want?\n"))
dice_sides = int(input("How many sides your dices have?\n"))
roll_amount = int(input("How many throws?\n"))

results = throw(dice_amount, dice_sides, roll_amount)
print(results)

