namesList = ["Abdul", "James", "Steves", "Soger","Tony"]

startsWithS = False

for name in namesList:
    if(name.lower().startswith('s')):
        startsWithS = True
        print(f"{name}")

if not startsWithS:
    print("no names starting with S")