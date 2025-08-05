#WAP to swap two numbers without using third variable.

x=int(input("Enter 1st number:"))
y=int(input("Ënter 2nd number:"))
print(f'before swap x:{x} y:{y}')

#x=x+y
#y=x-y
#x=x-y
x,y=y,x

print(f'After swap x:{x} y:{y}')