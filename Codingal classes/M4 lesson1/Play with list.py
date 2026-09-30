L = [5, 10, 1, 7, 9, 3, 12]
print("Original list:", L)

count = 0
for i in L:
    count += 1

avg = count / len(L)

print("sum = ", count)
print("average = ", avg)

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])
