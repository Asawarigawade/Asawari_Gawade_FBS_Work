lenght=int(input("Enter length:"))
breadth=int(input("Enter bredth:"))
radius=int(input("Enter radius:"))

area=(lenght+breadth) +(1/2*3.14*(breadth/2)**2)
perimeter =(2*lenght)+breadth * (3.14*breadth/2)

print(f'Area:{area},perimeter:{perimeter}')