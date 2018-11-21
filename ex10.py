def main():
    recurse(1)

def recurse(times):
    print("This is a recursive function.")

    if times < 5:
        recurse(times + 1)

main()