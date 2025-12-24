numbers = []
for i in range(9):
    numbers.append(int(input(f"{i+1}] ")))

unique = set(numbers)
print(f"\nUnique numbers from {numbers} are: {unique}")

#--------------

sett = {18,'18'}
print(sett) #yes possible to have int of 18 and string of 18

#--------------------

s = set()
s.add(20)
s.add(20.0) # stores unique elements based on equality ($==$) and hash values, and they both share the same hash value ($hash(20) == hash(20.0)$)
s.add('20')
print(f"Set is : {s} and length is {len(s)}") #Output is 2

s = {}
print(type(s)) #dict