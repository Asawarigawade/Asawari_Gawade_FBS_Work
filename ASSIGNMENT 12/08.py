# 8. Remove the Characters of Odd Index Values in a String
s8 = "abcdef"
print("".join(s8[i] for i in range(len(s8)) if i % 2 == 0))
