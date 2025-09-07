Dictionary = {'a': 'happy', 'b': 'birthday', 'c': 'to', 'd': 'you', 'e': 'dear'}
key_to_remove = 'e'
if key_to_remove in Dictionary:
    del Dictionary[key_to_remove]
print("Dictionary after removing the given key:", Dictionary)