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
                while aagoptionstown3 not in "run outside,find authority":
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
                    else:
                        print("I'm sorry I do not understand")
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
                    else:
                        print("I'm sorry I do not understand")
            else:
                print("I'm sorry I do not understand")
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
        while aagoptions2cave not in ["fight", "run"]:
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
                You manage to fit through as the bBar growls on the other side.
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
                            else:
                                print("I'm sorry I do not understand")
                    else:
                        print("I'm sorry I do not understand")
            else:
                print("I'm sorry I do not understand")
    elif aagoptions1 == "right":
        print('''
        You went right and towards a mountain.
        It is a very tall mountain and there seems to be a climbing axe.
        Someone unfortunate must have left it here.
        You take the axe anyways.
        ''')
    else:
        print("I'm sorry I do not understand")