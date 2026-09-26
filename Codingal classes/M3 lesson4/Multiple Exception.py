try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError as ex:
    print("ZeroDivisionError Exception:", ex)
except ValueError as ex:
    print("ValueError Exception:", ex)
except Exception as ex:
    print("General Exception:", ex)
else:
    print("No exception occurred")
finally:
    print("This will always execute no matter what")