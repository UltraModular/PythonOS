import sys
import time
import random

class MyTime:
    def __init__(self, numbertime:int) -> str:
        if numbertime == 1:
            timed = time.time()
        if numbertime == 2:
            timed = time.localtime()
        self.timed = timed
        

    # Gives you the time
    def mTime(self, hourtime:int):
        hour = self.timed[3]
        minute = self.timed[4]
        if minute < 10:
            minute = f"0{minute}"
        if hourtime == 1:
            if hour == 0:
                hour += 12
            elif hour > 12:
                return f"{str(hour - 12)}:{str(minute)} pm"
            return f"{str(hour)}:{minute} am"
        elif hourtime == 2:
            return  f"{str(hour)}:{minute}"
        else:
            if hour == 0:
                hour += 12
            elif hour > 12:
                return f"{str(hour - 12)}:{str(minute)} pm"
            return f"{str(hour)}:{minute} am"


    # Gives you the weekday
    def mWeekDate(self):
        weekdays = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        weekday = self.timed[6]
        return f"{weekdays[weekday]}"

    # Gives you the date
    def mDate(self):
        year = self.timed[0]
        month = self.timed[1]
        day = self.timed[2]
        return f"{day}/{month}/{year}"


    # Gives you the amount of weeks that have passed since this year
    def mWeeks(self):
        weeks = self.timed[7]
        return f"{round(weeks / 7)}"


class CSpoken(MyTime):
    def __init__(self, number:int):
        super().__init__(number)
        
    
    # Just gives the time as what would have been said by a person
    def FTime(self, options:int):
        return f"Today is {MyTime.mWeekDate(self)}, {MyTime.mDate(self)}. It is {MyTime.mTime(self, options)}."
    
    def SpokenTime(self, options:int):
        return f"It is currently {MyTime.mTime(self, options)}."

    def Date(self):
        return f"Today is {MyTime.mDate(self)}." 

    def WDate(self):
        return f"Today is {MyTime.mWeekDate(self)}."

    def Week(self):
        if self.options in ["", 1]:
            return f"Week {MyTime.mWeeks(self)}."
        if self.options == 2:
            return f"It is Week {MyTime.mWeeks(self)}."


def iof(number) -> int:
    y = isinstance(number, float)
    if y != True:
        number = int(number)
    else:
        number = float(number)
    return number


def riddler(riddlechooser:random, riddles:list, number:int, answer:str, riddle:str):
    if riddlechooser == number:
        riddlea = None
        while riddlea != answer:
            riddlea = input(riddle).capitalize
            if riddlea == answer:
                print("You got that one correct!")
                riddles.remove(number)
                break


def calculateang(a, b, formula) -> str:
    if formula == 1:
        sum = a ** 2 + b ** 2
        sum **= 2
        return f'''
    formula = a^2 + b^2 = c^2
    {sum} = ({a}^2 + {b}^2)^2
    '''
    if formula == 2:
        pass


def slow_type(text:str, speed:int) -> str:
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)


def makeaccount(userinterface, logins:dict, extra:int):
    keys = logins.keys()
    if userinterface in keys:
        password3 = None
        attempts = []
        password2 = 3
        if extra == 2 or extra == 12:
            if userinterface == "Ian":
                hint = ""
        while password3 != logins[userinterface]:
            password3 = input("Enter the password: ")
            attempts.append(password3)
            if password3 != logins[userinterface]:
                if extra == 1 or extra == 12:
                    password2 -= 1
                    print(f"Attempts remaning: {password2}")
                if extra == 2 or extra == 12:
                    #hint system
                    print(f"Hint: {hint}")
                print("Your password is incorrect. Attempts:")
                for a in attempts:
                    print(a)
            if extra == 1 or extra == 12:
                if password2 == 0:
                    print(f"You are not {userinterface}. Goodbye.")
                    quit()
        if userinterface != "Guest":
            print("Correct password. Welcome back!")
        else: 
            print("Welcome to PythonOS!")


def calculate(x:int, y:int, operator:str) -> str:
    # calculates
    match operator:
        case ["+"]:
            sum = x + y
        case ["-"]:
            sum = x - y
        case ["*"]:
            sum = x * y
        case ["/"]:
            sum = x / y
    if operator in ["+", "-", "*", "/"]:
        return f'{x} {operator} {y} = {sum}'
    match operator:
        case ["5", "%"]:
            sum = 100 * x / y
            return f'{x}% of {y} is {sum}'
        case ["6", "^"]:
            sum = x ** y
            return f'{x} raised to the power of {y} = {sum}'
        case ["7", "√"]:
            sum = iof(x ** 0.5)
            return f'The square root of {x} = {sum}'

loginbook = {
    # "User" : "Password"
    "Ian" : "password",
    "Guest" : None
}

PyOS = ["Booting up PythonOS. \n", "Booting up PythonOS.. \n", "Booting up PythonOS... \n"]
slow_type((PyOS[0] + PyOS[1] + PyOS[2]) * 3, 500)
userinterface = ""
while userinterface not in ["Guest", "Ian"]:
    userinterface = str(input("\nWhich user? \nIan \nGuest \n")).capitalize()
    try:
        makeaccount(userinterface, loginbook, 1)
    except TypeError:
        print(f"There is no user called {userinterface}.")
while True:
    timed = CSpoken(2)
    print("Welcome")
    print(timed.FTime(1))
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
            mathcheck = input("\nWhich Calculator?\nBasic\nGeometric\n")
            if mathcheck in ["Calculator", "calculator"]:
                # Calculator
                # Improvements: finished
                choice = None
                print("Hello this is a calculator")
                loop = int(input("How many times you want to loop the program? "))
                calnum1 = iof(input("Put the first number here: \n"))
                for i in range(loop):
                    if choice == ["7", "√"]:
                        calnum1 = iof(input("Put the first number here: \n"))
                    choice = str(input(f'''
Which mathmatical symbol?
(+ = 1, - = 2, x = 3, / = 4)
(% = 5, ^ = 6, √ = 7)
                    '''))
                    if choice in ["1", "+"]:
                        choice = "+"
                    elif choice in ["2", "-"]:
                        choice = "-"
                    elif choice in ["3", "*", "x"]:
                        choice = "*"
                    elif choice in ["4", "/"]:
                        choice = "/"
                    if choice in ["5", "%"]:
                        calnum2 = iof(input(f"{calnum1}% of? "))
                    elif choice in ["6", "^"]:
                        calnum2 = iof(input(f"{calnum1} raised to the power of: "))
                    elif choice not in ["7", "√", "%", "5"]:
                        calnum2 = iof(input(f"{calnum1} {choice} "))
                    else:
                        print("um put the right numbers next time")
                        break
                    print(calculate(calnum1, calnum2, choice))
                    loop =- 1
                    if loop == 0:
                        break
                    if loop > 0:
                        choice2 = input("Are you done with your calculations? (Y/N) ").capitalize()
                        if choice2 == "Yes":
                            break
                        else: 
                            if choice != ["7", "√"]:
                                calnum1 = sum
                            print(f"Amount of loops left: {loop}")
            if mathcheck in ["Angles"]:
                print("Hello this is an angles calculator")
                calangle = int(input('''
Which mathmatical theorem?
( **put numbers only** )
1 = Pythagoras
2 =
                '''))
                if calangle == 1:
                    angnum1 = iof(input("Input the first side: "))
                    angnum2 = iof(input("Input the second side: "))
                    print(calculateang(angnum1, angnum2, 1))
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
                if riddleinput in ["yes", "y", "Yes"]:
                    riddle = {
                        1: "Riddle: I am tall when I am young, and I am short when I am old.\nWhat am I?\n",
                        2: "Riddle: What flows and has banks?\n",
                        3: "Riddle: In the morning, I walk on 4 legs. In the afternoon, I walk on 2 legs. At night, I walk on 3 legs. What am I?\n",
                        4: "Riddle: \n"
                    }
                    riddleanswers = {
                        1: "Candle",
                        2: "Lake",
                        3: "Human",
                        4: ""
                    }
                    riddles = [1, 2]
                    while True:
                        riddlechooser = random.choice(riddles)
                        riddles = [1, 2, 3]
                        riddler(riddlechooser, riddles, 1, riddleanswers[1], riddle[1])
                        riddler(riddlechooser, riddles, 2, riddleanswers[2], riddle[2])
                        riddler(riddlechooser, riddles, 3, riddleanswers[3], riddle[3])
                        riddler(riddlechooser, riddles, 4, riddleanswers[4], riddle[4])
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
