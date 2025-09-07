def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def armstrong(num, order):
    if num == 0:
        return 0
    return power(num % 10, order) + armstrong(num // 10, order)

num = 153
order = len(str(num))
print("Armstrong:", armstrong(num, order) == num)