# 13. Count the Occurrence of Each Word in a String
s13 = "apple orange apple banana orange"
words13 = s13.split()
word_count13 = {}
for word in words13:
    word_count13[word] = word_count13.get(word, 0) + 1
print(word_count13)
