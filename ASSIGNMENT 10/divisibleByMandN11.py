lst=[30,40,50]
m, n = 2, 3
for i in lst:
    if i % m == 0 and i % n == 0:
        print(i, "is divisible by", m, "and", n)