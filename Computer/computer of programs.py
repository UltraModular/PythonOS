import sys
import time
import random
import math
import datetime as dt
from dateutil.tz import gettz


def iof(number):
    y = isinstance(number, float)
    if y != True:
        number = int(number)
    else:
        number = float(number)
    return number


def riddler(number, answer, riddle):
    if riddlechooser == number:
        riddlea = None
        while riddlea != answer:
            riddlea = input(riddle)
            if riddlea == answer:
                print("You got that one correct!")
                riddles.remove(number)
                break


def slow_type(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)


def makeaccount(user, password, extra):
    if userinterface in [user]:
        password3 = None
        attempts = []
        password2 = 3
        if extra == 2 or extra == 12:
            if user == "Ian":
                hint = ""
        while password3 != password:
            password3 = input("Enter the password: ")
            attempts.append(password3)
            if password3 != password:
                if extra == 1 or extra == 12:
                    password2 = password2 - 1
                    print(f"Attempts remaning: {password2}")
                if extra == 2 or extra == 12:
                    #hint system
                    print(f"Hint: {hint}")
                print("Your password is incorrect. Attempts:")
                for a in attempts:
                    print(a)
            if extra == 1 or extra == 12:
                if password2 == 0:
                    print(f"You are not {user}. Goodbye.")
                    sys.exit()
        print("Correct password. Welcome back!")


def calculate(x, y, operator):
    # calculates
    if operator in ["+", "1"]:
        sum = x + y
    if operator in ["-", "1"]:
        sum = x - y
    elif operator in ["*", "x", "1"]:
        sum = x * y
    elif operator == ["/", "4"]:
        sum = x / y
    return f'{x} {operator} {y} = {sum}'


IanOS1 = "Booting up IanOS. \n"
IanOS2 = "Booting up IanOS.. \n"
IanOS3 = "Booting up IanOS... \n"
slow_type((IanOS1 + IanOS2 + IanOS3) * 3, 500)
datatime = False
datatimesettings1 = False
userinterface = ""
while userinterface not in ["Guest", "Ian"]:
    userinterface = input("\nWhich user? \nIan \nGuest \n")
    makeaccount("Ian", "password", 12)
    if userinterface in ["Guest"]:
        print("Welcome!")
    elif userinterface not in ["Guest", "Ian"]:
        print(f"There is no user called {userinterface}")
while True:
    if not datatime:
        ddatatime = dt.datetime.now(gettz('Australia/Melbourne'))
        dddatatime = f"Today is {ddatatime:%D %A %I:%M %p}"
        print(dddatatime)
        if not datatimesettings1:
            datatime = True
    program = input('''
    Which program? 
    1. Math 
    2. PaintINDEV 
    3. GamesIndev 
    4. Other ProgramsINDev 
    Exit?
    ''')
    if program in ["Math", "math", "1"]:
        mathcheck = None
        while mathcheck is None:
            mathcheck = input("\nWhich program?\n")
            if mathcheck in ["Calculator", "calculator"]:
                # Calculator
                # Improvements: finished
                print("Hello this is a calculator")
                loop = int(input("How many times you want to loop the program? "))
                calnum1 = iof(input("Put the first number here: \n"))
                for i in range(loop):
                    choice = input(f'''
                    Which mathmatical symbol?
                    (+ = 1, - = 2, x = 3, / = 4)
                    (% = 5, ^ = 6, √ = 7)
                    ''')
                    if choice in ["5", "%"]:
                        calnum2 = iof(input(f"{calnum1}% of? "))
                    if choice not in ["7", "√", "%", "5"]:
                        calnum2 = iof(input(f"{calnum1} {choice} "))
                    if choice in ["1", "+"]:
                        choice = "+"
                    elif choice in ["2", "-"]:
                        choice = "-"
                    elif choice in ["3", "*", "x"]:
                        choice = "*"
                    elif choice in ["4", "/"]:
                        choice = "/"
                    if choice not in ["7", "√", "%", "5"]:
                        print(calculate(calnum1, calnum2, choice))
                    elif choice in ["5", "%"]:
                        sum = 100 * calnum1 / calnum2
                        print(f'{calnum1}% of {calnum2} = {sum}')
                    elif choice in ["6", "^"]:
                        sum = calnum1 ** calnum2
                        print(f'{calnum1} raised to the power of {calnum2} = {sum}')
                    elif choice in ["7", "√"]:
                        sum = math.sqrt(calnum1)
                        print(f'The square root of {calnum1} = {sum}')
                        break
                    else:
                        print("um put the right numbers next time")
                        break
                    loop = loop - 1
                    if loop == 0:
                        break
                    if loop > 0:
                        choice2 = input("Are you done with your calculations? (Y/N) ")
                        if choice2 == "yes":
                            break
                        else: 
                            choice = None
                            calnum2 = None
                            calnum1 = sum
                            print(f"Amount of loops left: {loop}")
            if mathcheck in ["Angles"]:
                print("angle")
    elif program in ["Paint", "paint", "2"]:
        # Paint
        # Improvements: pen is finished
        print("Welcome to Paint")
        paintquit2 = False
        while not paintquit2:
            paintinput = input("Start? (Y/N) ")
            if paintinput in ["yes", "Yes"]:
                print("Sorry no")
            elif paintinput in ["no", "No", "n", "N"]:
                break
            else:
                print("I'm sorry I do not understand.")
    elif program in ["Games", "games", "3"]:
        # Games
        # Improvements: Add more games
        print("Welcome to Games")
        while True:
            gameinput = int(input('''Choose which game you want to play:
            0. Quit
            1. Riddles
            2. Tic Tac Toe
            3. Text Adventure
            10. Next page...
            Game No.'''))
            if gameinput == 0:
                continue
            if gameinput == 1:
                riddleinput = input("Welcome to Riddles!\nDo you want to start?")
                if riddleinput == "yes":
                    print("sorry this is still WIP")
                    riddle1 = "Riddle: I am tall when I am young, and I am short when I am old.\nWhat am I?\n"
                    riddle2 = "Riddle: What flows and has banks?\n"
                    riddle3 = ""
                    riddleanswer1 = "candle"
                    riddleanswer2 = "lakes"
                    riddleanswer3 = ""
                    while True:
                        riddlechooser = random.choice(riddles)
                        riddles = [1, 2]
                        riddler(1, riddleanswer1, riddle1)
                        riddler(2, riddleanswer2, riddle2)
                        riddler(3, riddleanswer3, riddle3)
                        riddleyn = input('Want another riddle?')
                        if riddleyn in ['no', 'n']: 
                            print("Okay, see you later!")
                            break
            if gameinput == 2:
                print('Welcome to Tic Tac Toe!')
                tttinput1 = input('1. Single Player\n2.Multiplayer\n')
                if tttinput1 in ['Single Player', 'single player', '1']:
                    tttinput = input("Easy, Medium, Hard, Impossible? \nDifficulty: ")
                    if tttinput in ["impossible", "Impossible"]:
                        pass
            if gameinput == 3:
                gagenre = input('''
                Which genre?
                Adventure
                ''')
                if gagenre in ["Adventure", "adventure"]:
                    pass
            elif gameinput not in [1, 2, 3]:
                print("I'm sorry I do not understand")
    elif program in ["other programs", "programs", "Other programs", "Programs", "4"]:
        print("Which program?")
        inputprogram = int(input())
        if inputprogram in ["1"]:
            input()
    elif program in ["Settings", "settings", "4"]:
        settings = input("What settings?")
        if settings in ["time", "Time"]:
            settingsdt = input("What do you want to change?")
            if settingsdt in ["datatime"]:
                datatimesettings1 = True
            elif settingsdt in ["exit", "Exit"]:
                break
        if settings in ["help", "Help"]:
            print("dt: sets the time of the computer")
    elif program in ["shut down", "5", "quit", "stop", "exit"]:
        # Quits
        break
    else:
        print(f"I'm sorry. I do not understand this command: {program}")
print("Goodbye!")
