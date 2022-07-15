import time
import random

# Tell the time
class MyTime:
    def __init__(self, numbertime:int) -> str:
        if numbertime == 1:
            timed = time.time()
        if numbertime == 2:
            timed = time.localtime()
        self.timed = timed
        

    # Gives you the time
    def mTime(self, hourtime:int=1):
        hour, minute = self.timed[3], self.timed[4]
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

    # Gives you the parts of the day
    def SpokenTime2(self):
        hour = self.timed[3]
        if hour == 0:
            return "Midnight"
        elif hour < 12 and hour != 0:
            return "Morning"
        elif hour == 12:
            return "Noon"
        elif hour > 12 and hour < 18:
            return "Afternoon"
        elif hour > 17 and hour < 21:
            return "Night"

    # Gives you the weekday
    def mWeekDate(self):
        weekdays, weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"], self.timed[6]
        return f"{weekdays[weekday]}"

    # Gives you the date
    def mDate(self):
        return f"{self.timed[0]}/{self.timed[1]}/{self.timed[2]}"


    # Gives you the amount of weeks that have passed since this year
    def mWeeks(self) -> int:
        return int(self.timed[7] // 7)

# Tell the time (like a human being)
class CSpoken(MyTime):
    def __init__(self, number:int=2):
        super().__init__(number)
        
    
    # Just gives the time as what would have been said by a person
    def FSpokenTime(self, options:int=1):
        return f"Today is {MyTime.mWeekDate(self)}, {MyTime.mDate(self)}. It is {MyTime.mTime(self, options)}."
    
    def SpokenTime(self, options:int=1):
        return f"It is currently {MyTime.mTime(self, options)}."

    def SpokenDate(self):
        return f"Today is {MyTime.mDate(self)}." 

    def SpokenWDate(self):
        return f"Today is {MyTime.mWeekDate(self)}."

    def SpokenWeek(self, options=None):
        if options == 1 or options == None:
            return f"Week {MyTime.mWeeks(self)}."
        if options == 2:
            return f"It is Week {MyTime.mWeeks(self)}."

# just returns integer or float lmao
def iof(number) -> int:
    y = isinstance(number, float)
    if y != True: number = int(number)
    else: number = float(number)
    return number

# delaying the amount in the list to be print
def delaysleepl(list:list, howmuch:int, howlong:float):
    for i in range(howmuch):
        x = 0
        for items in list:
            print(list[x])
            x += 1
            time.sleep(howlong)

# make account in login framework
def makeaccount(userinterface, logins:dict):
    keys = logins.keys()
    if userinterface in keys:
        password2, password3 = 3, None
        while password3 != logins[userinterface]:
            print(f"Attempts remaning: {password2}")
            password3 = input("Enter the password: ")
            if password3 != logins[userinterface]:
                password2 -= 1
                print(f"{password3} is incorrect.")
            if password2 == 0:
                raise Exception(f"\nYou are not {userinterface}. Goodbye.")
        if userinterface != "Guest":
            print("\nCorrect password. Welcome back!")
        else: 
            print("\nWelcome to PythonOS!")

# used for calculating
def calculate(x:int, y:int, operator:str) -> str:
    # calculates
    if operator in ["+"]: sum = x + y
    elif operator in ["-"]: sum = x - y
    elif operator in ["*"]: sum = x * y
    elif operator in ["/"]: sum = x / y
    if operator in ["+", "-", "*", "/"]: return f'\n{x} {operator} {y} = {sum}'
    elif operator in ["5", "%"]:
        sum = 100 * x / y
        return f'\n{x}% of {y} is {sum}'
    elif operator in ["6", "^"]:
        sum = x ** y
        return f'\n{x} raised to the power of {y} = {sum}'
    elif operator in ["7", "√"]:
        sum = iof(x ** 0.5)
        return f'\nThe square root of {x} = {sum}'

# used for calculating angles (+ turtle)
def calculateang(a, b, formula) -> str:
    if formula == 1:
        sum = a ** 2 + b ** 2
        sum **= 2
        a /= 10
        b /= 10
        return f"formula = a^2 + b^2 = c^2\n{sum} = ({a}^2 + {b}^2)^2"
    if formula == 2: pass

# used for riddle game
def riddler(riddles:dict, howmany:int=None):
    if howmany == None:
        howmany = len(riddles.keys()) - 1
    riddlechooser = random.randint(0, howmany)
    riddlea, riddleb, riddlec = None, list(riddles.values()), list(riddles.keys())
    print(riddlec)
    print(riddleb)
    while riddlea != riddleb[riddlechooser]:
        riddlea = input(riddlec[riddlechooser]).capitalize()
        if riddlea == riddleb[riddlechooser]:
            print("You got that one correct!")
            break

# Introduction
PyOS = ["Booting up PythonOS.", "Booting up PythonOS..", "Booting up PythonOS..."]
delaysleepl(PyOS, 3, 0.5)
print("Booted up!")

# Login framework
loginbook = { # "User" : "Password"
    "Guest" : None, "Ian" : "password" }
logonbook, userinterface = list(loginbook.keys()), None
print()
while userinterface not in logonbook:
    print("Users:")
    for i in logonbook:
        print(f"{i}")
    userinterface = str(input("\nWhich user? \n")).capitalize()
    makeaccount(userinterface, loginbook)
    if userinterface not in logonbook: print(f"There is no user called {userinterface}.")
programtime = CSpoken(2)
print(programtime.FSpokenTime(1))

# Main framework
while True:
    program = input('''
Which program? 
1. Math 
2. PaintINDEV 
3. GamesIndev 
4. Other ProgramsINDev 
Exit?\n''').capitalize()
    if program in ["Math", "1"]:
        while True:
            mathcheck = input("\nWhich Calculator?\n\nBasic\nGeometric\nProgrammer\nOr just quit\n").capitalize()
            if mathcheck == "Basic":
                mathmatical, calnum2 = [None, "+", "-", "*", "/", "%", "^", "√"], None
                print("\nHello. This is a Calculator.")
                loop = int(input("How many times do you want to loop the program? "))
                calnum1 = iof(input("Put the first number here: \n"))
                for i in range(loop):
                    choice = str(input(f'''Which mathmatical symbol?
(+ = 1, - = 2, * = 3, / = 4)
(% = 5, ^ = 6, √ = 7)\n'''))
                    if choice == "x": choice = "*"
                    if choice.isnumeric(): choice = mathmatical[int(choice)]
                    if choice == "%": calnum2 = iof(input(f"{calnum1}% of? "))
                    elif choice == "^": calnum2 = iof(input(f"{calnum1} raised to the power of: "))
                    elif choice == "√": pass
                    elif choice not in ["√", "%"]: calnum2 = iof(input(f"{calnum1} {choice} "))
                    else:
                        print("um put the right numbers next time")
                        break
                    print(calculate(calnum1, calnum2, choice))
                    loop -= 1
                    if loop == 0: break
                    elif loop > 0:
                        choice2 = input("Are you done with your calculations? (Y/N)\n").capitalize()
                        if choice2 in ["Yes", "Y"]: break
                        else: 
                            if choice != ["7", "√"]: calnum1 = sum
                            print(f"Amount of loops left: {loop}\n")
            elif mathcheck in ["Geometric", "Angles"]:
                print("Hello. This is an Angles Calculator with Turtle. Check your other window to see results.")
                calangle = int(input('''
Which mathmatical theorem?
( **put numbers only** )
1 = Pythagoras
2 =\n'''))
                if calangle == 1:
                    angnum1, angnum2 = iof(input("Input the first side: ")), iof(input("Input the second side: "))
                    print(calculateang(angnum1, angnum2, 1))
            elif mathcheck == "Programmer":
                pass
            elif mathcheck == "Quit": break
            else: print("Sorry, I do not understand.")
    elif program in ["Paint", "2"]:
        print("Welcome to Paint")
        while True:
            paintinput = input("Start? (Y/N) ")
            if paintinput in ["yes", "Yes"]:
                print("Sorry no")
                break
            elif paintinput in ["no", "No", "n", "N"]: break
            else: print("I'm sorry I do not understand.")
    elif program in ["Games", "3"]: # Improvements: Add more games
        print("Welcome to Games")
        while True:
            gameinput = int(input('''Choose which game you want to play:
0. Quit
1. Riddles
2. Tic Tac Toe
3. Text Adventure
10. Next page...
Game No.'''))
            if gameinput == 0: continue
            if gameinput == 1:
                riddleinput = input("Welcome to Riddles!\nDo you want to start?")
                if riddleinput in ["yes", "y", "Yes"]:
                    riddles = {
                        # Riddle : Answer
                        "Riddle: I am tall when I am young, and I am short when I am old.\nWhat am I?\n" : "Candle",
                        "Riddle: What flows and has banks?\n" : "Lakes",
                        "Riddle: In the morning, I walk on 4 legs. In the afternoon, I walk on 2 legs. At night, I walk on 3 legs. What am I?\n" : "Human",
                        "Riddle: \n" : ""
                    }
                    while True:
                        # random choose in the dictionary and then select from the dictionary
                        riddler(riddles, 2)
                        riddleyn = input('Want another riddle?')
                        if riddleyn in ['no', 'n']: 
                            print("Okay, see you later!")
                            break
            if gameinput == 2:
                print('Welcome to Tic Tac Toe!')
                tttinput1 = input('1. Single Player\n2.Multiplayer\n')
                if tttinput1 in ['Single Player', 'single player', '1']:
                    tttinput = input("Easy, Medium, Hard, Impossible? \nDifficulty: ")
                    if tttinput in ["impossible", "Impossible"]: pass
            if gameinput == 3:
                gagenre = input('''
Which genre?
Adventure
''')
                if gagenre in ["Adventure", "adventure"]: pass
            elif gameinput not in [1, 2, 3]:
                print("I'm sorry I do not understand")
    elif program in ["Other programs", "Programs", "4"]:
        print("Which program?")
        inputprogram = int(input())
        if inputprogram in ["1"]: input()
    elif program in ["Settings", "4"]:
            settings = input("What settings?")
            if settings in ["time", "Time"]:
                settingsdt = input("What do you want to change?")
                if settingsdt in ["datatime"]:
                    datatimesettings1 = True
            elif settingsdt in ["exit", "Exit"]:
                break
            if settings in ["help", "Help"]:
                print("dt: sets the time of the computer")
    elif program in ["Shut down", "Quit", "Stop", "Exit"]: break # Quits
    else: print(f"I'm sorry. I do not understand this command: {program}")
print("Goodbye!")
