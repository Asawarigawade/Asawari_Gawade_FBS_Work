lst=[3,9,7,4,3]
x = int(input("Enter element to search: "))
count = 0
for i in lst:
    if i == x:
        count += 1
if count > 0:
    print(x, "is present", count, "times")
else:
    print(x, "not present")
