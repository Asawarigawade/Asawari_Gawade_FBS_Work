s12 = "banana"
freq12 = {}
for ch in s12:
    freq12[ch] = freq12.get(ch, 0) + 1
print(freq12)
