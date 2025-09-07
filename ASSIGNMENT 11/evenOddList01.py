lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in lst1 if x % 2 == 0]
odd = [x for x in lst1 if x % 2 != 0]
print("Even list:", even)
print("Odd list:", odd)

