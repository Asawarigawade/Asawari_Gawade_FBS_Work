lst=[2,6,7,9,5,4]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even List:", even)
print("Odd List:", odd)