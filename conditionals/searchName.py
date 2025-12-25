names_dic = [
    'james',
    'hulk',
    'barner',
    'abdul',
    'steves'
]

name = input("Enter a name to search : ")

if name.lower() in names_dic:
    print(f"Name {name} exists in the names dictionary")
else:
    print(f"Name {name} doesn't exists in the names dictionary")