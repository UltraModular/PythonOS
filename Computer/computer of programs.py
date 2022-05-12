import sys,time,random,turtle,math
from tokenize import Exponent
from tkinter import Y
import datetime as dt
from dateutil.tz import gettz
from turtle import *
def slow_type(text, speed):
    typing_speed = speed
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
def makeaccount(user, password):
    if userinterface in [user]:
        password3 = None
        attempts = []
        password2 = 3
        while password3 != password:
            password3 = input("Enter the password: ")
            attempts.append(password3)
            if password3 != password:
                password2 = password2 - 1
                print("Your password is incorrect. Attempts:")
                for i in attempts:
                    print(i)
            if password2 == 0:
                print(f"You are not {user}. Goodbye.")
                sys.exit()
        print("Correct password.")
        print("Welcome back!")
IanOS1 = ("Booting up IanOS. \n")
IanOS2 = ("Booting up IanOS.. \n")
IanOS3 = ("Booting up IanOS... \n")
slow_type((IanOS1 + IanOS2 + IanOS3) * 3, 500)
print("Welcome!")
datatime = False
datatimesettings1 = False
userinterface = ""
while userinterface not in ["guest", "Guest", "Ian", "ian"]:
    userinterface = input("\nWhich user? \nIan \nGuest \n")
    userinterface.capitalize()
    makeaccount("Ian", "password")
    if userinterface in ["Guest"]:
        print("Welcome!")
    elif userinterface not in ["Guest", "Ian"]:
        print(f"There is no user called {userinterface}")
while True:
    if datatime == False:
        ddatatime = dt.datetime.now(gettz('Australia/Melbourne'))
        dddatatime = f"Today is {ddatatime:%D %A %I:%M %p}"
        print(dddatatime)
        if datatimesettings1 != True: 
            datatime = True
    program = input("Which program? \n1. Math \n2. PaintINDEV \n3. GamesIndev \n4. Other ProgramsINDev \nExit?\n")
    program.capitalize()
    if program in ["Math", "1"]:
        while True:
            mathcheck = input("\nWhich program? \nCalculator \nPercentage \nExponentiation\n")
            mathcheck.capitalize()
            if mathcheck in ["Calculator"]:
                # Calculator
                # Improvements: finished
                print("Hello this is a calculator")
                loop = int(input("How many times you want to loop the program? "))
                calnum1 = float(input("Put the first number here: \n"))
                for i in range(loop):
                    choice = input("Which mathmatical symbol?\n(+ = 1, - = 2, x = 3, / = 4)\n(^ = 5, % = 6, √ = 7)\n")
                    if choice not in ["7", "√"]:
                        calnum2 = float(input("Put the second number here: \n"))
                    if choice in ["1", "+"]:
                        sum = calnum1 + calnum2
                        print(f'{calnum1} + {calnum2} = {sum}')
                    elif choice in ["2", "-"]:
                        sum = calnum1 - calnum2
                        print(f'{calnum1} - {calnum2} = {sum}')
                    elif choice in ["3", "*", "x"]:
                        sum = calnum1 * calnum2
                        print(f'{calnum1} * {calnum2} = {sum}')
                    elif choice in ["4", "/"]:
                        sum = calnum1 / calnum2
                        print(f'{calnum1} / {calnum2} = {sum}')
                    elif choice in ["5", "^"]:
                        sum = calnum1 ** calnum2
                        print(f'{calnum1}raised to the power of {calnum2} is {sum}')
                    elif choice in ["6", "%"]:
                        sum = 100 * calnum1 / calnum2
                        print(f'{calnum1}% of {calnum2} is {sum}')
                        break
                    elif choice in ["7", "√"]:
                        sum = math.sqrt(calnum1)
                        print(f'The square root of {calnum1} is {sum}')
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
                            print(f"Amount of loops left: {loop}")
    elif program in ["Paint", "2"]:
        # Paint
        # Improvements: pen is finished
        print("Welcome to Paint")
        paintquit2 = False
        while paintquit2 != True:
            paintinput = input("Start? (Y/N) ")
            paintinput.capitalize
            if paintinput in ["Yes", "Y"]:
                paintquit = False
                while paintquit != True:
                    options = input("Choose what you want to do: \nDraw \nPen Colour \nPaint Bucket \nExit \n")
                    options.capitalize()
                    if options in ["draw", "pen"]:
                        penoptions = input("How much for the pen? \nTurn the pen \nLeft or Right? \nMove the pen \nForward or Backwards? \n")
                        penoptions2 = float(input("How much or what colour/color?"))
                        if penoptions in ["Left", "Turn left", "Go left"]:
                            left(penoptions2)
                        if penoptions in ["Right", "Turn right", "Go right"]:
                            right(penoptions2)
                        elif penoptions in ["Forward", "Go foward"]:
                            forward(penoptions2)
                        elif penoptions in ["Backwards", "Back", "Go backwards", "Backward", "Go backward"]:
                            def backward(x):
                                right(180)
                                forward(x)
                            backward(penoptions2)
                    elif options in ["Color", "Pen colour"]:
                        paintcolour = input("Which color?")
                        pencolor(paintcolour)
                    elif options in ["Paint bucket", "Bucket"]:
                        paintcolour = input("Which color?")
                        fillcolor(paintcolour)
                    elif options in ["Quit", "Exit", "Leave"]:
                        paintquit2 = True
                        break
            elif paintinput in ["no", "No", "n", "N"]:
                break
            else: print("I'm sorry I do not understand.")
    elif program in ["Games", "3"]:
        # Games
        # Improvements: Add more games
        print("Welcome to Games")
        while True:
            gameinput = int(input("Choose which game you want to play:\n0. Quit\n1. Riddles\n2. Tic Tac Toe\n3. Text Adventure\n10. Next page...\nGame No."))
            if gameinput == 0:
                continue
            if gameinput == 1:
                riddleinput = input("Welcome to Riddles!\nDo you want to start?")
                if riddleinput == "yes":
                    def riddler(number, answer, riddle):
                        if riddlechooser == number:
                            riddleanswer1 = (answer)
                            riddle1 = ('')
                            while riddle != riddleanswer1:
                                riddle1 = input(riddle)
                                if riddle1 == riddleanswer1:
                                    print("You got that one correct!")
                                    riddles.remove(number)
                                    break
                    print("sorry this is still WIP")
                    riddles = 1, 2
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
                        print(" _  _  _\n _  _  _\n _  _  _")
                        tttinput1 = int(input("Choose a number out of 9: "))
                        if tttinput1 == 1:
                            print(" X  _  _\n _  _  _\n _  _  _")
                            tttinput2 = int(input("Player 2! Number:"))
                            if tttinput2 == 2:
                                print
            if gameinput == 3:
                    gagenre = input("Which genre? \nAdventure \n")
                    if gagenre in ["Adventure", "adventure"]:
                        aagwin = 0
                        print('''
                        [Story by Ian and Adrian]
                        You have decided to go on an adventure all by yourself!
                        You may never come back. 
                        You will probably die as there is very low chance any adventurer to survive. 
                        So adventurer what will you do?...
                        ''') 
                        print("Use help if you don't know any commands")
                        aagoptions1 = ""
                        while aagoptions1 not in ["backwards", "forward", "left", "right"]:
                            aagoptions1 = input("")
                            aagoptions1.capitalize
                            if aagoptions1 == "Help":
                                print("Forward = go forward \nBackwards = go backwards \nLeft = turn left \nRight = turn right")
                            elif aagoptions1 == "Backwards":
                                print('''
                                You decided to go back home.
                                You had enough adventure for today.
                                ''')
                                break
                            elif aagoptions1 == "Forward":
                                print('''
                                You continue onward.
                                You found a town.
                                Bustling streets and smells of freshly baked food makes you feel like an joyful early morning sunrise.
                                You wonder deeper into the town until you found an alleyway.
                                There's an inn.
                                You booked a room and start to sleep.
                                But that's not really what happened, is it?
                                You couldn't sleep.
                                Get up from the bed?
                                ''')
                                aagoptions1 = ""
                                while aagoptionstown2 not in ["Open the window", "Get up"]:
                                    aagoptionstown2 = input("")
                                    aagoptionstown2.capitalize
                                    if aagoptionstown2 == "Help":
                                        print("Open the window = open the window next to your bed \nget up = get up from the bed")
                                    if aagoptionstown2 == "Open the window":
                                        print(''' 
                                        You hear loud sounds towards the window and open it.
                                        It appears that there is a commotion happening. 
                                        You hear men arguing about a certain scheme going on.
                                        You keep on listening. 
                                        You realise they are plotting to steal.
                                        They plan to rob the town of all its precious money and gold from the town bank.
                                        ''')
                                        aagoptionstown3 = ""
                                        while aagoptionstown3 not in ("run outside,find authority"):
                                            aagoptionstown33 = input("")
                                            if aagoptionstown33 == "run outside":
                                                print(''' you run out the building but its too late the men have already left 
                                                all you see on the ground is a peice of paper,on it its wirten 32 tiky lane cenarto st.
                                                you go my to a near merchant he sells u map.
                                                but it is a ripoff and cost over 1 billion (inworld) currency
                                                what do u do
                                                ''')
                                            if aagoptionstown33 == "find authority":
                                                print(''' 
                                                You run outside to find police but oops car crash
                                                ''')
                                    if aagoptionstown2 == "Get up":
                                        print('''
                                        You got up from the bed.
                                        You feel groggy.
                                        You left the inn.
                                        Where are you going?
                                        You went into the alleyway.
                                        What are you doing?
                                        There is a door.
                                        Should you open it?
                                        ''')
                                        aagoptionstown32 = ""
                                        while aagoptionstown32 not in ("help", "yes", "no"):
                                            aagoptionstown32 = input("")
                                            if aagoptionstown32 == "Help":
                                                print("Yes = ope           n door No = dont open door")
                                            if aagoptionstown32 == "Yes":
                                                print('''
                                                You had a mental breakdown in front of the door.
                                                You thought of how bad you are at stopping the theives.
                                                (Hint: Don't open the door idiot)
                                                ''')
                                            if aagoptionstown32 == "No":
                                                print('''
                                                You regain your mind and thought through things.
                                                You went back to inn and slept.
                                                The next morning, you decided you had enough adventure and went back home.
                                                (Hint: Listen to your own instincts)
                                                ''')
                                            else: print("I'm sorry I do not understand")
                                        while aagoptionstown3 not in ("help", "return to sleep", "stop them"):
                                            aagoptionstown3 = input("")
                                            aagoptionstown3.capitalize()
                                            if aagoptionstown3 == "help":
                                                print("return to sleep = go back to sleep \nstop them = stop the thieves")
                                            if aagoptionstown3 == "return to sleep":
                                                print(''' 
                                                You fumble to sleep but people outside get supecious.
                                                As your curtaints are not closed, you hear commotion about them saying that they think someone may have heard.
                                                Suddenly you hear the doors of the inn open and footsteps up the stairs.
                                                Many men in suits enter your room and say "Sorry Chap but it appears you have heard too much."
                                                He pulls out a pistol and it's the end for you.
                                                (Hint: Be smarter and stop them idiot)
                                                ''')
                                                break
                                            if aagoptionstown3 == "stop them":
                                                print('''
                                                ''')
                                            else: print("I'm sorry I do not understand")
                                    else: print("I'm sorry I do not understand")
                            elif aagoptions1 == "left":
                                print('''
                                You went to the left and found a dark cave.
                                Welcome to the Cave.
                                It is freezing cold.
                                Icicles have formed at the top of the cave.
                                All you can hear is the sound of bats wings flapping.
                                The dark is nearing as the sun is setting.
                                You see bright lights from a nearby town.
                                Suddenly you hear something heavy breathing.
                                What is it?
                                In the dark, your eyes adjusted to the dark and found there is a sleeping Bear!
                                What will you do?
                                ''')
                                aagoptions2cave = ""
                                while aagoptions2cave not in ["fight" ,"run"]:
                                    aagoptions2cave = input("")
                                    if aagoptions2cave == "help":
                                        print("fight = fight the Bear", "run = run away")
                                    if aagoptions2cave == "fight":
                                        print('''
                                        You jump forward to attack the Bear.
                                        The commotion you are making wakes the Bear.
                                        The Bear is frightened and acts upon your feeble body.
                                        The Bear absoulutly mauls you and tears your body into shreads.
                                        Why would you do that?
                                        (Hint: get a weapon next time idiot.
                                        Also don't die.)
                                        ''')
                                        break
                                    if aagoptions2cave == "run":
                                        print('''
                                        The Bear wakes up but luckily you manage to find a crack in the cave.
                                        You manage to fit through as the bBar growles on the other side.
                                        The Bear tries to find you but you manage to not get spotted.
                                        The Bear sleeps once more.
                                        In the crack, you find a pickaxe that was left behind the person before you.
                                        What will you do?
                                        ''')
                                        aagoptions3cave = ""
                                        while aagoptions3cave not in ["fight", "sneak"]:
                                            aagoptions3cave = input("")
                                            if aagoptions3cave == "help":
                                                print("fight = take the pickaxe and fight, sneak = sneak out")
                                            if aagoptions3cave == "sneak":
                                                print('''
                                                You have successfully snuck out of the cave.
                                                ''')
                                            if aagoptions3cave == "fight":
                                                print('''
                                                You have now obtained a weapon! (pickaxe) 
                                                You have a good chance at killing the Bear.
                                                You are able to sneak though the crack and sneak over to the Bear's head.
                                                You gather all your strenghth and in one big swing you kill the Bear.
                                                You have now killed your enemy.
                                                What will you do now?
                                                ''')
                                                aagoptions4cave = ""
                                                while aagoptions4cave not in ["leave"]:
                                                    aagoptions4cave = input("")
                                                    if aagoptions4cave == "leave":
                                                        print('''
                                                        
                                                        ''')
                                                    else: print("I'm sorry I do not understand")
                                            else: print("I'm sorry I do not understand")
                                    else: print("I'm sorry I do not understand")
                            elif aagoptions1 == "right":
                                print('''
                                You went right and towards a mountain.
                                It is a very tall mountain and there seems to be a climbing axe.
                                Someone unfortunate must have left it here.
                                You take the axe anyways.
                                ''')
                            else: print("I'm sorry I do not understand")
            elif gameinput not in [1, 2, 3]:
                print("I'm sorry I do not understand")
    elif program in ["Other Programs", "Programs", "4"]:
        print("Which program?")
        inputprogram = int(input())
        if inputprogram in ["1"]:
            input()
    elif program in ["Settings", "4"]:
        settings = input("What settings?")
        settings.capitalize()
        if settings in ["Time"]:
            settingsdt = print("What do you want to change?")
            if settingsdt in ["datatime"]:
                datatimesettings1 = True
            elif settingsdt in ["exit", "Exit"]:
                break
        if settings in ["Help"]:
            print("dt: sets the time of the computer")
    elif program in ["Shut down", "5", "Quit", "Stop"]:
        #Quits
        break
    else: print(f"I'm sorry. I do not understand this command: {program}")
print("Goodbye!")