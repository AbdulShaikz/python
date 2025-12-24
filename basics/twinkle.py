import requests
import os

print('Twinkle Twinkle Little Star, \nHow I wonder what you are!')

#For printing 5 table in REPL
"""
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
"""

response = requests.get('https://www.google.com')

print("Type is\t:\t",type(response))

print("Response is\t:\t",response.status_code)

directory_path = '.'
print(os.listdir(directory_path))
print(type(os.path))
print(f"Contents of dir '{os.path.abspath(directory_path)}'")