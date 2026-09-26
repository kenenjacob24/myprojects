try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")   