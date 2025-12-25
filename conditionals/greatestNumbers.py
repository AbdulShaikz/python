numbers = []
while True:
    try:
        a = int(input("Enter a number (or press Enter to stop): "))
        numbers.append(a)
    except ValueError:
        break

if numbers:
    print(f"Greatest number: {max(numbers)}")
    print(f"All numbers: {numbers}")