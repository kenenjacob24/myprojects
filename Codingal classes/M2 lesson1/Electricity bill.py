units = int(input(" Please enter Number of Units you Consumed: "))

if(units<50):
    Amount = units * 2.60
    surcharge = 25

elif(units <= 100):
    Amount = 130 + ((units-50) * 3.25)
    surcharge = 35

elif(units <= 200):
    Amount = 130 + 162.5 + ((units-100) * 5.26)
    surcharge = 45

else:
    Amount = 130 + 162.5 + 526 + ((units-200) * 8.50)
    surcharge = 75

total = Amount + surcharge
print("\n Electricity Bill = %.2f" %total)
