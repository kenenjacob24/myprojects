actual_cost = float(input("please enter the actual cost: "))
sale_price = float(input("please enter the selling price: "))

if (sale_price > actual_cost):
    amount = sale_price - actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No profit!!!")