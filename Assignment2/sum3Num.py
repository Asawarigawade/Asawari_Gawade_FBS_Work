
num = int(input("Enter a 3-digit number: "))


hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
digit_sum = hundreds + tens + ones


print(f"Sum of digits = {digit_sum}")