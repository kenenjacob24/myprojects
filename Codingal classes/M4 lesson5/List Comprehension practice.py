num = int(input("Enter a number:    "))
print([n for n in range(1, num) if n % 2 == 0])
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print([f.capitalize() for f in fruits if 'a' in f])