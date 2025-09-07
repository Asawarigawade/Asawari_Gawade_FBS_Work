lst4 = [17, 13, 20, 15, 11]
for i in range(len(lst4)):
    for j in range(len(lst4)-1-i):
        if lst4[j] > lst4[j+1]:
            lst4[j], lst4[j+1] = lst4[j+1], lst4[j]
print("Second largest (bubble sort):", lst4[-2])
