import time
from math import log
from random import randint
# Tell the time
class MyTime:
    def __init__(self, numbertime:int) -> str:
        if numbertime == 1: timed = time.time()
        if numbertime == 2: timed = time.localtime()
        self.timed = timed
        
    # Gives you the time
    def mTime(self, hourtime:int=1):
        hour, minute = self.timed[3], self.timed[4]
        if minute < 10: minute = f"0{minute}"
        if hourtime == 1:
            if hour == 0: hour += 12
            elif hour > 12: return f"{str(hour - 12)}:{str(minute)} pm"
            return f"{str(hour)}:{minute} am"
        elif hourtime == 2: return  f"{str(hour)}:{minute}"

    # Gives you the parts of the day
    def SpokenTime2(self):
        hour = self.timed[3]
        if hour == 0: return "Midnight"
        elif hour < 12 and hour != 0: return "Morning"
        elif hour == 12: return "Noon"
        elif hour > 12 and hour < 18: return "Afternoon"
        elif hour > 17 and hour < 21: return "Night"

    # Gives you the weekday
    def mWeekDate(self):
        weekdays, weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"], self.timed[6]
        return f"{weekdays[weekday]}"

    # Gives you the date
    def mDate(self): return f"{self.timed[0]}/{self.timed[1]}/{self.timed[2]}"

    # Gives you the amount of weeks that have passed since this year
    def mWeeks(self) -> int: return int(self.timed[7] // 7)
# Tell the time (like a human being)
class CSpoken(MyTime):
    def __init__(self, number:int=2) -> str: super().__init__(number)
        
    def FSpokenTime(self, options:int=1): return f"Today is {MyTime.mWeekDate(self)}, {MyTime.mDate(self)}. It is {MyTime.mTime(self, options)}."
    
    def SpokenTime(self, options:int=1): return f"It is currently {MyTime.mTime(self, options)}."
    
    def SpokenDate(self): return f"Today is {MyTime.mDate(self)}." 

    def SpokenWDate(self): return f"Today is {MyTime.mWeekDate(self)}."

    def SpokenWeek(self, options=1):
        if options == 1: return f"Week {MyTime.mWeeks(self)}."
        if options == 2: return f"It is Week {MyTime.mWeeks(self)}."
# delaying the amount in the list to be print
def delaysleepl(list:list, howmuch:int, howlong:float) -> str:
    for long in range(howmuch):
        x = 0
        for items in list:
            print(list[x])
            x += 1
            time.sleep(howlong)
# make account in login framework
def makeaccount(userinterface:str, logins:dict):
    keys = logins.keys()
    if userinterface in keys:
        password2, password3 = 3, None
        while password3 != logins[userinterface]:
            print(f"Attempts remaning: {password2}")
            password3 = input("Enter the password: ")
            if password3 != logins[userinterface]:
                password2 -= 1
                print(f"{password3} is incorrect.")
            if password2 == 0: raise Exception(f"\nYou are not {userinterface}. Goodbye.")
        if userinterface != "Guest":
            print("\nCorrect password. Welcome back!")
        else: 
            print("\nWelcome to PythonOS!")
# just returns integer or float from float lmao
def iof(number:float) -> int | float:
    number = float(number)
    y = number.is_integer()
    if y: number = int(number)
    return number
# calculates into int or float
def calculation(x:int | float, y:int | float, operator:str) -> int | float:
    if operator == "+": sumd = iof(x + y)
    elif operator == "-": sumd = iof(x - y)
    elif operator == "*": sumd = iof(x * y)
    elif operator == "/": sumd = iof(x / y)
    elif operator == "%": sumd = iof(100 * x / y)
    elif operator == "^": sumd = iof(x ** y)
    elif operator == "√": sumd = iof(x ** 0.5)
    elif operator == "logarithm": sumd = log(x, y)
    return sumd
# calculates into string
def calculate(x:int | float, y:int | float, operator:str) -> str:
    sumd = calculation(x, y, operator)
    if operator in ["+", "-", "*", "/"]: return f'\n{x} {operator} {y} = {sumd}'
    elif operator == "%": return f'\n{x}% of {y} is {sumd}'
    elif operator == "^": return f'\n{x} raised to the power of {y} = {sumd}'
    elif operator == "√": return f'\nThe square root of {x} is {sumd}'
    elif operator == "logarithm": return f'\nlog{y}({x}) = {sumd}'
# used for calculating angles (+ turtle)
def calculateang(a: int | float, b: int | float, formula:int, formula2:int) -> str:
    if formula == 1:
        if formula2 == 1:
            sumd = a ** 2 + b ** 2
            sumd **= 2
            return f"Pythagoras Formula: a^2 + b^2 = c^2\n{sumd} = ({a}^2 + {b}^2)^2"
    if formula == 2: pass
# used for riddle game
def riddler(riddles:dict, howmany:int=None):
    if howmany == None:
        howmany = len(riddles.keys()) - 1
    riddlechooser = randint(0, howmany)
    riddlea, riddleb, riddlec = None, list(riddles.values()), list(riddles.keys())
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
while userinterface not in loginbook:
    print("Users:")
    for i in logonbook: print(f"{i}")
    userinterface = str(input("\nWhich user? \n")).capitalize()
    makeaccount(userinterface, loginbook)
    if userinterface not in loginbook: print(f"There is no user called {userinterface}.\n")
print(CSpoken(2).FSpokenTime(1))
# Main framework
programs = [None, "Math", "Paint", "Games", "Other Programs", "Settings"]
while True:
    program = input('''Which program? 
1. Math 
2. PaintINDEV 
3. GamesIndev 
4. Other ProgramsINDev 
5. SettingsINDev
Exit?\n''').capitalize()
    if program.isnumeric(): program = programs[int(program)]
    if program == "Math":
        while True:
            mathcheck = input("\nWhich Calculator?\nArithmetic\nTrigometric\nProgrammer\nOr just quit\n").capitalize()
            if mathcheck == "Arithmetic":
                mathmatical, calnum2 = [None, "+", "-", "*", "/", "%", "^", "√", "logarithm"], None
                print("\nHello. This is an Arithmetic Calculator.")
                loop = int(input("How many times do you want to loop the program? "))
                for i in range(loop):
                    if calnum2 == None: calnum1 = iof(input("Put the first number here: \n"))
                    choice = str(input(f'''Which mathmatical symbol?
(+ = 1, - = 2, * = 3, / = 4)
(% = 5, ^ = 6, √ = 7, logarithm = 8\n'''))
                    if choice == "x": choice = "*"
                    if choice.isnumeric(): choice = mathmatical[int(choice)]
                    if choice == "%": calnum2 = iof(input(f"{calnum1}% of? "))
                    elif choice == "^": calnum2 = iof(input(f"{calnum1} raised to the power of: "))
                    elif choice == "logarithm": calnum2 = iof(input(f"What is the anti-logarithm? ")) 
                    elif choice not in ["√", "%", "log"]: calnum2 = iof(input(f"{calnum1} {choice} "))
                    else: raise ValueError("um put the right numbers next time")
                    sumd = calculation(calnum1, calnum2, choice)
                    print(calculate(calnum1, calnum2, choice))
                    loop -= 1
                    if loop == 0: break
                    elif loop > 0:
                        choice2 = input("Are you done with your calculations? (Y/N)\n").capitalize()
                        if choice2 in ["Yes", "Y"]: break
                        else: 
                            choose = input("Do you want to keep the sum as the first number?\n").capitalize()
                            if choose in ["Y", "Yes"]: calnum1 = sumd
                            else: calnum2 = None
                            print(f"Amount of loops left: {loop}\n")
            elif mathcheck in ["Trigometric", "Geometric", "Angles"]:
                print("Hello. This is an Angles Calculator with Turtle. Check your other window to see results.")
                calchoice = int(input('''
Which kind of angle?
( **put numbers only** )
1 = Right Angle Triangles\n'''))
                if calchoice == 1:
                    calangle1, calangle2, calangle3 = iof(input("1st Angle|Side: ")), iof(input("2nd Angle|Side: ")), iof(input("3rd Angle|Side (optional): "))
                    calchoice1 = int(input('''
Which kind of formula?
1 = Pythagoras
2 = SohCahToa'''))
                    calculateang()
            elif mathcheck == "Programmer": pass
            elif mathcheck == "Quit": break
            else: print("Sorry, I do not understand.")
    elif program == "Paint":
        print("Welcome to Paint")
        while True:
            paintinput = input("Start? (Y/N) ")
            if paintinput in ["yes", "Yes"]: print("no")
            elif paintinput in ["no", "No", "n", "N"]: break
            else: print("I'm sorry I do not understand.")
    elif program == "Games": # Improvements: Add more games
        print("Welcome to Games")
        while True:
            games = ["Quit", "Riddles", "Tic Tac Toe", "Text Adventure", None, None, None, None, None, None, "Next"]
            gameinput = str(input('''Choose which game you want to play:
0. Quit
1. Riddles
2. Tic Tac Toe
3. Text Adventure
10. Next page...\n''')).capitalize()
            if gameinput.isnumeric(): gameinput = games[int(gameinput)]
            if gameinput == "Quit": break
            elif gameinput == "Riddles":
                riddleinput = input("Welcome to Riddles!\nDo you want to start?")
                if riddleinput in ["yes", "y", "Yes"]:
                    riddles = { # Riddle : Answer
                        "Riddle: I am tall when I am young, and I am short when I am old.\nWhat am I?\n" : "Candle",
                        "Riddle: What flows and has banks?\n" : "Lakes",
                        "Riddle: In the morning, I walk on 4 legs. In the afternoon, I walk on 2 legs. At night, I walk on 3 legs. What am I?\n" : "Human",
                        "Riddle: \n" : ""
                    }
                    while True:
                        riddler(riddles, 2)
                        riddleyn = input('Want another riddle?')
                        if riddleyn in ['no', 'n']: 
                            print("Okay, see you later!")
                            break
            elif gameinput == "Tic Tac Toe":
                print('Welcome to Tic Tac Toe!')
                tttinput1 = input('1. Single Player\n2.Multiplayer\n')
                if tttinput1 in ['Single Player', 'single player', '1']:
                    tttinput = input("Easy, Medium, Hard, Impossible? \nDifficulty: ")
                    if tttinput in ["impossible", "Impossible"]: pass
            elif gameinput == "Text Adventure":
                gagenre = str(input('''
Which genre?
Adventure\n'''))
                if gagenre in ["Adventure", "adventure"]: pass
            else: print("I'm sorry I do not understand")
    elif program in ["Other programs", "Other Programs", "Programs"]:
        inputprograms = ["Quit", "Fibonacci"]
        while True:
            inputprogram = str(input("\nWhich program?\n0. Quit\n1. Fibonacci Sequence\nProgram No."))
            if inputprogram.isnumeric(): inputprogram = inputprograms[int(inputprogram)]
            if inputprogram in ["Fibonacci", "Fibonacci Sequence", "Fibonacci sequence"]: 
                Fibonacci, Fibonacci1, Fibonacci2 = int(input("\nHow long shall the Sequence be? ")), 0, 1
                print("Fibonacci Seqeunce:")
                for i in range(Fibonacci + 1):
                    print(f"{i}: {Fibonacci1}")
                    Fibonacci3 = Fibonacci1 + Fibonacci2
                    Fibonacci1, Fibonacci2 = Fibonacci2, Fibonacci3
                print()
            if inputprogram == "Quit": break
    elif program == "Settings":
        while True:
            settings = input("What settings?").capitalize()
            if settings == "Time":
                settingsdt = input("What do you want to change?").capitalize()
                if settingsdt == "Datatime":
                    pass
                elif settingsdt == "Exit": break
            elif settings == "Help": print("dt: sets the time of the computer")
            elif settings == "Quit": break
    elif program in ["Shut down", "Quit", "Stop", "Exit"]: break # Quits
    else: print(f"I'm sorry. I do not understand this command: {program}")
print("Goodbye!")
