string = input("Enter a string: ")
if "  " in string:
    print("There is a double space in the string")
    print(string.replace("  ", " "))
else:
    print("Alright!")