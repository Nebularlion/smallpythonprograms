print("KPH", " " * 12, "MPH")
print("-" * 20)

kph = 60
conversion = 0.62137119

for kph in range(60, 131, 10):
    mph = kph * conversion
    print(kph, " " * 12, round(mph, 1))

