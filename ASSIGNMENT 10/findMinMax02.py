lst=[4,8,9,5,3]
maxi = lst[0]
mini = lst[0]
for i in lst:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print("Max:", maxi, "Min:", mini)
