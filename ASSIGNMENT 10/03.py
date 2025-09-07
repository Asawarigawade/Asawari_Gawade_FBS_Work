lst=[1,3,8,9]
largest = second = lst[0]
for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second Largest:", second)