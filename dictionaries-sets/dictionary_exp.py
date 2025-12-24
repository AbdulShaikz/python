dictionary = {}

for i in range(4):
    name = input("Enter name : ")
    language = input("Enter language : ")
    dictionary[name] = language

print(dictionary) #if keys same it will overwrite prev value of the key, values can be same 

#s = {8, 7, 12, "Harry", [1, 2]}, Python will throw a TypeError: unhashable type: 'list'.
# Sets require "Hashable" items: For a set to quickly find and store unique elements, every item inside it must be hashable.
# Immutability: An object is only hashable if its value never changes during its lifetime.
# Lists are Mutable: Since you can change, add, or remove items from a list, its "content" is not fixed. Therefore, a list is unhashable and cannot be a member of a set.
