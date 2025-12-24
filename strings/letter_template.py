import datetime

name = input("Enter your name : ")
letter = f'''
Dear {name},
You are selected!
{str(datetime.datetime.today())[:10]}'''
print(letter)