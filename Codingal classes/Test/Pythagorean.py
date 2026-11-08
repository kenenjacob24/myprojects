import math

print("Pythagorean Theorem Calculator")
print("1.Find the Hypotenuse")
print("2.Find a missing side")

choice = int(input("Choose 1 or 2: "))

if choice == 1:
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = math.sqrt(a**2 + b**2)
    print("The length of the hypotenuse is:", c)

elif choice == 2:
    c = float(input("Enter the length of the hypotenuse: "))
    a = float(input("Enter the length of side a: "))
    b = math.sqrt(c**2 - a**2)
    print("The length of side b is:", b)

else:
    print("Invalid choice")
    
