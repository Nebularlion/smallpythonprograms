sales = []
i = 0
print("Enter the sales for each day.")

for i in range(1, 6):
    sale = input("Day #" + str(i) + ": ")
    sales.append(sale)

print("Here are values you entered:")
for y in sales:
    print(float(y))