test_dict = {'a': 1, 'b': 2, 'c': 3}
print(test_dict)
value = input("Enter a value to check: ")
if value in test_dict.values():
    print(f"{value} is present in the dictionary.")
else:
    print(f"{value} is not present in the dictionary.")
    
