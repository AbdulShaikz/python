num = int(input('Enter num : '))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("\nReversed order:")
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")