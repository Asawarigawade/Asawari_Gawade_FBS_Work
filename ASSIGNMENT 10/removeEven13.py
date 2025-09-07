lst=[4,6,7,3,6]
odd_list = []
for i in lst:
    if i % 2 != 0:
        odd_list.append(i)
print("List after removing even numbers:",odd_list)