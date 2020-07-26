string = input("input the string: ")
if len(string) >= 3:
    result = string[0:-2]
    print(type(result))
    print("first five characters: ", result)
else:
    print("string is too small")
