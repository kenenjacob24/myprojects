def square_number(start, end):
    number = list(range(start, end + 1))
    squared_numbers = [n ** 2 for n in number]

    odd = [n for n in squared_numbers if n % 2 != 0]
    even = [n for n in squared_numbers if n % 2 == 0]

    print("Odd squares:", odd)
    print("Even squares:", even)
    print("All squares:", squared_numbers)

square_number(1, 10)