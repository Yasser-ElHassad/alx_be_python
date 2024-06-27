pattern_size = int(input("Enter the size of the pattern: "))
count = pattern_size
while count > 0:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    count  -= 1
