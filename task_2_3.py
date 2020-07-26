string = input("input the string: ")
if len(string) >= 5:
    result = string[0:5]
    print("first five characters: ", result)
else:
    print("string is too small")
