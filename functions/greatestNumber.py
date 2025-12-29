def findGreatest(values):
    maxValue = values[0]
    for value in values:
        if value>maxValue:
            maxValue=value
    print(f"The Greatest Value is : {maxValue}")

values = list(map(int, input("Enter numbers : ").split(" ")))
findGreatest(values)
