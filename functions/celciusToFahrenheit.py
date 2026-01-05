def convertToFah(celcius):
    return (celcius*1.8)+32

temp = int(input("Enter celcius : "))
print(f'{temp}℃ <==> {convertToFah(temp)}℉',end="")