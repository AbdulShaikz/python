def pattern(n):
    for i in range(n):
        stars = "* "*(n-i)
        print(stars)

n = int(input("Enter n level : "))
pattern(n)