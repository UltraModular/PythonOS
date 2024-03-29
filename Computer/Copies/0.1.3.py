import sys,time,random
typing_speed = 500 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
from turtle import *
IanOS1 = ("Booting up IanOS. \n")
IanOS2 = ("Booting up IanOS.. \n")
IanOS3 = ("Booting up IanOS... \n")
slow_type((IanOS1 + IanOS2 + IanOS3) * 3)
print("Welcome!")
userinterface = ()
while userinterface not in ["guest", "Guest", "Ian", "ian"]:
    userinterface = input("\nWhich user? \nIan \nGuest \n")
    if userinterface in ["Ian", "ian"]:
        password = None
        attempts = []
        amountattempts = {3}
        while password != "password":
            password = input("Enter the password: ")
            attempts.append(password)
            if password != "password":
                print("Your password is incorrect. Attempts:")
                for i in attempts:
                    print(i)
        print("Correct password.")
        print("Welcome back!")
        break
    elif userinterface in ["Guest", "guest"]:
        print("Welcome!")
        break
    elif userinterface not in ["guest", "Guest", "Ian", "ian"]:
     print("There is no user called "+userinterface+".")
while True:
    print("Which program? \n1. Calculator \n2. PaintINDEV \n3. GamesIndev \n4. Other Programs \nExit?")
    program = input()
    if program in ["calculator", "1"]:
        # Calculator
        # Improvements: finished
        print("Hello this is a calculator")
        loop = int(input("How many times you want to loop the program? "))
        for i in range(loop):
            calnum1 = float(input("Put the first number here \n"))
            calnum2 = float(input("Put the second number here \n"))
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
            elif print("um put the right numbers next time"):
                break
            print(sum)
            loop = loop - 1
            if loop == 0:
                break
            if loop > 0:
                choice2 = input("Are you done with your calculations? (Y/N) ")
                if choice2 == "yes":
                    break
                else: print("Amount of loops left:")
                print(loop)
    elif program in ["paint", "2"]:
        # Paint
        # Improvements: InDev
        print =("Welcome to Paint")
        paintquit2 = False
        while paintquit2 != True:
            paintinput = input("Start? (Y/N) ")
            if paintinput in ["yes", "y", "Yes", "Y"]:
                paintquit = False
                while paintquit != True:
                    options = input("Choose what you want to do: \nDraw \nPen Colour \nPaint Bucket \nExit \n")
                    if options in ["draw", "pen"]:
                        penoptions = input("Turn the pen \nLeft or Right? \nMove the pen \nForward or Backwards?")
                        penoptions2 = float(input("How much or what colour/color?"))
                        if penoptions in ["left", "turn left", "go left"]:
                            left(penoptions2)
                        if penoptions in ["right", "turn right", "go right"]:
                            right(penoptions2)
                        elif penoptions in ["forward", "go foward"]:
                            forward(penoptions2)
                        elif penoptions2 in ["backwards", "back", "go backwards", "backward", "go backward"]:
                            def backward(x):
                                right(180)
                                forward(x)
                            backward(penoptions2)
                    elif options in ["color", "pen colour", "pen color"]:
                        paintcolour = input("Which color?")
                        pencolor(paintcolour)
                    elif options in ["paint bucket", "bucket"]:
                        fillcolor(penoptions2)
                    elif options in ["quit", "exit", "leave"]:
                        break
            elif paintinput in ["no", "No", "n", "N"]:
                break
            else: print("I'm sorry I do not understand.")
    if program in ["games", "3"]:
        # Games
        # Improvements: Add more games
        print("Welcome to Games")
        print("Choose which game you want to play \n0. Quit \n1. Riddles \n2. Tic Tac Toe \n3. Text Adventure \n10. Next page...")
        gameinput = input("Game No.")
        gameinput = int(gameinput)
        if gameinput == 0:
            continue
        if gameinput == 1:
            print("Welcome to Riddles!")
            riddleinput = input("Do you want to start?")
            if riddleinput == "yes":
                print("sorry this is still WIP")
                continue
                riddle1 = input("Riddle: I’m tall when I’m young, and I’m short when I’m old. \n What am I?")
                riddleanswer1 = ("candle")
                riddle2 = input("what flows and has banks")
                riddleanswer2 = ("lakes")
                riddlechooser = range(riddle1)
                if riddle1 == riddleanswer1:
                    print("You got that one correct!")
                if riddle2 == riddleanswer2:
                    print("You got that one correct!")
        if gameinput == 2:
            tttinput = input("Easy, Medium, Hard, Impossible? \nDifficulty: ")
            if tttinput in ["impossible", "Impossible"]:
                print()
        if gameinput == 3:
            gagenre = input("Which genre? \nAdventure \n")
            if gagenre in ["Adventure", "adventure"]:
                aagwin = 0
                print('''
                [Story by Ian andAdrian]
                You have decided to go on an adventure all by yourself!
                You may never come back. 
                You will probably die as there is very low chance any adventurer to survive. 
                So adventurer what will you do?...
                ''')
                print("Use help if you don't know any commands")
                aagoptions1 = ""
                while aagoptions1 not in ["help", "backwards", "forward", "left", "right"]:
                    aagoptions1 = input("")
                    if aagoptions1 == "help":
                        print("forward = go forward \nbackwards = go backwards \nleft = turn left \nright = turn right")
                    elif aagoptions1 == "backwards":
                        print('''
                        You decided to go back home.
                        You had enough adventure for today.
                        ''')
                        break
                    elif aagoptions1 == "forward":
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
                        while aagoptionstown2 not in ["open the window", "get up"]:
                            aagoptionstown2 = input("")
                            if aagoptionstown2 == "help":
                                print("open the window = open the window next to your bed \nget up = get up from the bed")
                            if aagoptionstown2 == "open the window":
                                print(''' 
                                You hear loud sounds towards the window and open it.
                                It appears that there is a commotion happening. 
                                You hear men arguing about a certain scheme going on.
                                You keep on listening. 
                                You realise they are plotting to steal.
                                They plan to rob the town of all its precious money and gold from the town bank.
                                ''')
                                aagoptionstown3 = ""
                            if aagoptionstown2 == "get up":
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
                                    if aagoptionstown32 == "help":
                                        print("yes or no")
                                    if aagoptionstown32 == "yes":
                                        print('''

                                        ''')
                                    if aagoptionstown32 == "no":
                                        print('''
                                        You regain your mind and thought through things.
                                        You went back to inn and slept.
                                        The next morning, you decided you had enough adventure and went back home.
                                        (Hint: Listen to your own instincts) 
                                        ''')
                                    else: print("I'm sorry I do not understand")
                                while aagoptionstown3 not in ("help", "return to sleep", "stop them"):
                                    aagoptionstown3 = input("")
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
                        while aagoptions2cave not in ["help","fight" ,"run"]:
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
                                while aagoptions3cave not in ["help", "fight", "sneak"]:
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
                                        while aagoptions4cave not in ["help", "leave"]:
                                            aagoptions4cave = input("")
                                            if aagoptions4cave == "leave":
                                                print('''
                                                ''')
                                            else: print("I'm sorry I do not understand")
                                    else: print("I'm sorry I do not understand")
                            else: print("I'm sorry I do not understand")
                    elif aagoptions1 == "right":
                        print('''
                        You went left and towards a mountain.
                        It is a very tall mountain and there seems to be a climbing axe.
                        Someone unfortunate must have left it here.
                        You take the axe anyways.
                        ''')
                    else: print("I'm sorry I do not understand")
    if program in ["other programs", "programs", "4"]:
        print("Which program?")
        inputprogram = input()
        if inputprogram in ["1"]:
            input()
    if program in ["shut down", "5", "quit", "stop"]:
        #Quit quits
        break
    if program not in ["shut down", "5", "quit", "stop", "other programs", "programs", "4", "games", "3", "paint", "2", "calculator", "1"]:
        print("I'm sorry. I do not understand this command: "+program+"")
print("Goodbye!")