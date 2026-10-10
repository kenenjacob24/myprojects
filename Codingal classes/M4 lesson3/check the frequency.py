test_dect = {'codigal' : 2, 'is' : 2, 'for' : 2, 'best' : 2, 'codigal' : 1}

print("The original dictionary : " + str(test_dect))

k = 2

res = 0
for key in test_dect:
    if test_dect[key] == k:
        res += 1

print("Frequency of k is : " + str(res))
