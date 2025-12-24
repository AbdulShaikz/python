# marks = list(map(int, input("Enter the marks of 9 students :").split(" ")))
marks = []

for i in range(0,9):
    marks.insert(i,int(input(f"Student {i+1} marks : ")))
marks.sort()
print(f"Sorted marks : {marks}")