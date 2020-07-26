string = input("input the string: ")
if len(string) <= 1:
    print("string is too small")
else:
    char = string[-2]
    print("the penultimate character of the string: ", char)