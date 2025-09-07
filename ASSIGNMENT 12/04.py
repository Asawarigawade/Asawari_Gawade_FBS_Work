
# 4. Form a New String with the First and Last Character Exchanged
s4 = "hello"
if len(s4) > 1:
    print(s4[-1] + s4[1:-1] + s4)
else:
    print(s4)
