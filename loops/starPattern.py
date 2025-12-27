'''
input: 5
output:
1. Pattern 1
    *
   * *
  * * *
 * * * *
* * * * *
2. Pattern 2
*
* *
* * *
* * * *
* * * * *
3. Pattern 3
* * * * *
*       *
*       *
*       *
* * * * *
'''
level = int(input("Enter level : "))
print('Pattern 1 : ')
for i in range(1, level+1):
    spaces = " " * (level-i)
    stars = "* " * i
    print(spaces + stars)
print('Pattern 2 : ')
for i in range (1, level+1):
    stars = ("* "*i)
    print(stars)
print("Pattern 3 : ")
for i in range (1,level+1):
    if i==1 or i==level:
        stars = "* " * level
        print(stars)
    else:
        spaces = " " * ((level-2)*2 )
        print("* " + spaces + "*")