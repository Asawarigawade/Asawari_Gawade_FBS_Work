lst=[5,9,7,5,6]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print("Without Duplicates:", unique)
