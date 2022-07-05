def asciiModule(number: int):
    z = str(chr(36) * number + chr(36) * 2)
    print(z)
    for l in range(number):
        print(str(chr(36) + chr(35) * number + chr(36)))
    print(z)

ascii1 = str(chr(36) * 2 * 2)
print(ascii1)
for l in range(2):
    print(str(chr(36) + chr(35) * 2 + chr(36)))
print(ascii1)

print()

ascii2 = str(chr(36) * 3 + chr(36) * 2)
print(ascii2)
for l in range(2):
    print(str(chr(36) + chr(35) * 3 + chr(36)))
print(ascii2)

print()

while True:
    while True:
        inputed = int(input("Input a number between 2 and 8"))
        if inputed > 2 and inputed < 8:
            asciiModule(inputed)
            print()
            break
    inputted = input("Do you want to print again?\n")
    if inputted == "yes":
        pass
    else: break
print("bye")