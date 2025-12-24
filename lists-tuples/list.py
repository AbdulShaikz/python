fruits = []
print("Enter the names of the fruits : \n")
for i in range(0,10):
    fruits.insert(i, input(f"{i+1}] : "))
print(f"The fruits basket contains\t:\n{str(fruits)}")