def iof(x):
    try: int(x)
    except ValueError: float (x)
calnum1 = input("Put the first number here \n")
iof(calnum1)
calnum2 = input("Put the second number here \n")
iof(calnum2)
choice = input("Which mathmatical symbol? \n(+ = 1, - = 2, x = 3, / = 4) \n")
if choice in ["1", "+"]:
    print('{}+{} = '.format(calnum1, calnum2))
    sum = calnum1 + calnum2
elif choice in ["2", "-"]:
    print('{}-{} = '.format(calnum1, calnum2))
    sum = calnum1 - calnum2
elif choice in ["3", "*", "x"]:
    print('{}*{} = '.format(calnum1, calnum2))
    sum = calnum1 * calnum2
elif choice in ["4", "/"]:
    print ('{}/{} = '.format(calnum1, calnum2))
    sum = calnum1 / calnum2
else:
    print("um put the right numbers next time")
iof(sum)
print(sum)