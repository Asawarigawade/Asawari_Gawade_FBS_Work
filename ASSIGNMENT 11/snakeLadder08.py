print("Snake and Ladder Pattern (1-100):")
for i in range(10):
    if i % 2 == 0:
        # Print left to right
        for j in range(1, 11):
            print(i*10 + j, end=' ')
    else:
        # Print right to left
        for j in range(10, 0, -1):
            print(i*10 + j, end=' ')
    print()
