classmates = {'Tony': 'cool but smells', 'Emma':'sits behind me', 'Lucy': 'ask too many questions'}   # key: Tony, value: cool but smells

print(classmates)
print(classmates['Emma'])
print(classmates['Tony'])

print("for loop:")
for key, value in classmates.items():
    print(key + " : " + value)