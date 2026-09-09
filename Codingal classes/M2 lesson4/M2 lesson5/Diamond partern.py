n = int(input("Enter the number of rows: "))
half = n // 2 + 1

for i in range(1, half + 1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

for i in range(half - 1, 0, -1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
