dict = {
    "tera": "your",
    "naam": "name",
    "kya": "what",
    "hai": "is"
}
print(type(dict))
search = input("Search english term for : ")

if search in dict.keys():
    print(f"{search} = {dict.get(search)}")
else:
    print("Not available in the the dictionary yet!")