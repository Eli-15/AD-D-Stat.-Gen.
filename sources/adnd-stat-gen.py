#!/usr/bin/python3
import random
import sys 

def method_1 ():
    rolls = []
    i = 0
    while (i<6):
        i = i + 1
        roll = []
        j = 0
        while (j < 4):
            j = j + 1
            roll.append( random.randint(1,6))
        roll.sort()
        rolls.append( sum(roll[1:]))
    print("Here's your stats. Thanks bye!", rolls)

def method_2 ():
    rolls = []
    i = 0
    while (i<12):
        i = i + 1
        roll = []
        j = 0
        while (j < 3):
            j = j + 1
            roll.append( random.randint(1,6))
        rolls.append( sum(roll))
    rolls.sort()
    print("Here's your stats. Thanks bye!",rolls[6:11])

def method_3 ():
    rolls = []
    i = 0
    while (i<6):
        i = i + 1
        stat = []
        j = 0
        while (j < 6):
            j = j + 1
            roll = []
            x  = 0
            while (x < 3):
                x = x + 1
                roll.append(random.randint(1,6))
            stat.append(sum(roll))
        stat.sort()
        rolls.append(stat[5])
    print("Here's your stats! Thanks bye! \nStr",rolls[0],"Dex", rolls[1], "Con", rolls[2], "Int", rolls[3], "Wis", rolls[4], "Char", rolls[5])

def method_4 ():
    charmatrix = []
    print("Choose one of the twelve characters below. Thanks bye!")
    character = 0
    while (character < 12 ):
        character = character + 1
        rolls = []
        i = 0
        while i < 6 :
            i = i + 1
            roll = []
            j = 0
            while j < 3:
                j = j + 1
                roll.append(random.randint(1,6))
            rolls.append(sum(roll))
        charmatrix.append( ["character", character, " Str", rolls[0], " Dex", rolls[1], " Con", rolls[2], " Int", rolls[3], " Wis", rolls[4], " Char", rolls[5]])
    for row in charmatrix:
        print("{:} {: >2} {: >5} {: >2} {: >5} {: >2} {: >5} {: >2} {: >5} {: >2} {: >5} {: >2} {: >5} {: >2}" .format(*row))



# start of the program!!!

#check for command line arg
if(len(sys.argv) == 2):
    if(sys.argv[1] == "1"):
        method_1()
        sys.exit(0)
    if(sys.argv[1] == "2"):
        method_2()
        sys.exit(0)
    if(sys.argv[1] == "3"):
        method_3()
        sys.exit(0)
    if(sys.argv[1] == "4"):
        method_4()
        sys.exit(0)

#default run mode
print("Hello! This program is a used to generate ability scores for AD&D characters using the methods found on page 11 of the DMG.\nSelect a method 1, 2, 3, or 4.\nJust type the number you want then hit 'enter' or you can quit by entering 'q'.")

loop = True

while ( loop == True ):
    loop = False
    method = input()
    
    if( method == '1'):
        method_1()
        sys.exit(0)
    elif ( method == '2'):
        method_2()
        sys.exit(0)
    elif ( method == '3'):
        method_3()
        sys.exit(0)
    elif ( method == '4'):
        method_4()
        sys.exit(0)
    elif ( method == 'q'):
        print("Thanks bye!")
        sys.exit(0)
    else :
        print("Invaled input. Please type a number between 1 and 4, or quit by entering 'q'")
        loop = True

#error check this line should never be run
sys.exit(1)
