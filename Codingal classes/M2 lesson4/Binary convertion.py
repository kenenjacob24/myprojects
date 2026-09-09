number = int(input("Enter a decimal number: "))

binary = ""
if number == 0:
    binary = "0"
else:
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2

print("Binary number: ", binary)