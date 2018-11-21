loop = True

while loop:
    cost = float(input("Enter the item's wholesale cost: "))
    if cost < 0:
        print("ERROR: the cost cannot be negative")
        cost = float(input("Enter the correct wholesale cost: "))
    else:
        print("Retail price ", cost + 0.75)

    looppi = input("Do you have another item? (Enter y for yes): ")

    if looppi == 'n':
        loop = False
    elif looppi == 'y':
        loop = True
