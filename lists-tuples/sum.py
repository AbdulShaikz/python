list = []
for i in range(0,4):
    list.insert(i,int(input(f"{i+1} : ")))

sum = 0
for i in list:
    sum += i
print(f'Sum of {list} is : {sum}')