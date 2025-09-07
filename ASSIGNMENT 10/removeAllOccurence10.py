lst=[5,9,4,8]
y = int(input("Enter element to remove: "))
new_list = []
for i in lst:
    if i != y:
        new_list.append(i)
print("List after removing", y, ":", new_list)
