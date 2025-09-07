numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]
print("Number\tSquare\tCube")
for i in range(10):
    print(f"{numbers[i]}\t{squares[i]}\t{cubes[i]}")
