'''
-------------------------------------------------------------------------------
///                        WELCOME
-------------------------------------------------------------------------------
'''

# -------- cls function clears the screen -----------
def cls():
    clS = '\n' * 100 # Simply write 100 blank lines :)
    print(clS)

print("This is a game where two player takes part")
print("Let's see who is the winner!\n")

'''
-------------------------------------------------------------------------------
///                        FIRST PLAYER
-------------------------------------------------------------------------------
'''
# -------- Ask for First Player's NAME -----------

fpN = '' # Set the fpN variable to a string
while True:
    try:
        fpN = str(input("First player's Name? "))
        if len(fpN) <= 3:
            print("I need your First name, and please do not use a number.\nTry again!\n")
        elif float(fpN) + float(fpN) >= 0 or float(fpN) + float(fpN) <= 0:
            print("Please do not use numbers in your name.\nTry again!\n")
        elif len(fpN) <= 3:
            print("Please enter a longer one. ")
    except:
        break # / IMPORTANT! Otherwise, keeps asking for User input.
    
cls() # Here is a function called

print("Hello, " + fpN + "! Welcome to this game! :)")



# -------- Ask for First Player's HEIGHT -----------

print("\nRight, now I need to know your height in centimeters.\nPlease enter only numbers.")

fph = 0

while True:
    try:
        fph = int(input("Your Height: ")) # Important to define it to 'int'. Otherwise, causes TypeError!
        if fph < 120:
            print("Are you a Dwarf " + fpN + "?\nTry again!")
            continue
        elif fph > 195:
            print("Are you a BF Giant " + fpN + "?\nTry again!")
            continue
        break
    except ValueError:
        print("Come on " + fpN + " Enter only numbers!")
        continue
print("Right, so you are " + str(fph) + " cm tall\n")

# -------- Ask for First Player's AGE -----------

print("Now and lastly, please tell me your age in years.\nAgain, please use only numbers.")
fpa = 0

while True:
    try:
        fpa = int(input("Your age: ")) # Important to define it to 'int'. Otherwise, causes TypeError!
        if fpa <= 7 :
            print("You are too young for this game.")
            q = ''
            q = input("Will you Play Again? (y/n) ")
            q = q.lower() # Set 'q' to lower case
            if q == 'y':
                continue
            elif q == 'n':
                print("Thank's to take part\nGood Bye!\nGame Over")
                exit()
            elif len(q) >= 2:
                print("Wrong answer\nGAME OVER")
                exit()
            else:
                print("Too young.\nGAME OVER")
                exit()
        elif fpa > 95:
            print("Too old")
            q = ''
            q = input("Will you Play Again? (y/n) ")
            q = q.lower()
            if q == 'y':
                continue
            elif q == 'n':
                print("Thank's to take apart\nGood Bye!\nGame Over")
                exit()
            elif q == 'n':
                print("Thank's to take apart\nGood Bye!\nGame Over")
                exit()
            elif len(q) >= 2:
                print("Wrong answer.\nGame Over!")
                exit()  
            else:
                print("Too old, EXIT")
                exit()
        break
    except ValueError:
        print("Come on Enter only numbers")
        continue
    
cls()

print("So we have " + fpN + ", who is " + str(fpa) + " years old, and " + str(fph) + " cm tall.")
print("\nNow Lets get second player's Details!")

'''
-------------------------------------------------------------------------------
///                        SECOND PLAYER
-------------------------------------------------------------------------------
'''
# -------- Ask for Second Player's NAME -----------

spN = '' # Set the spN variable to a string
while True:
    try:
        spN = str(input("Second player's Name? "))
        if len(spN) <= 3:
            print("I need your First name, and please do not use a number.\nTry again!\n")
        elif float(spN) + float(spN) >= 0 or float(spN) + float(spN) <= 0:
            print("Please do not use numbers in your name.\nTry again!\n")
        elif len(spN) <= 3:
            print("Please enter a longer one. ")
    except:
        break # / IMPORTANT! Otherwise keeps asking for User input

print("Hello, " + spN + "! Welcome to this game! :)")


# -------- Ask for Second Player's HEIGHT -----------

print("\nRight, now I need to know your height in centimeters.")

sph = 0

while True:
    try:
        sph = int(input("Your Height: ")) # Important to define it to 'int'. Otherwise causes TypeError!
        if sph < 120:
            print("Are you a Dwarf " + spN + "?\nTry again!")
            continue
        elif sph > 195:
            print("Are you a BF Giant " + spN + "?\nTry again!")
            continue
        break
    except ValueError:
        print("Come on " + spN + " Enter only numbers!")
        continue
print("Right, so you are " + str(sph) + " cm tall\n")

# -------- Ask for Second Player's AGE -----------

print("Now and lastly, please tell me your age in years.\nAgain, please use only numbers.")

spA = 0

while True:
    try:
        spA = int(input("Your age: ")) # Important to define it to 'int'. Otherwise causes TypeError!
        if spA <= 7 :
            print("You are too young for this game.")
            q = ''
            q = input("Will you Play Again? (y/n) ")
            q = q.lower()
            if q == 'y':
                continue
            elif q == 'n':
                print("Thank's to take apart\nGood Bye!\nGame Over")
                exit()
            elif len(q) >= 2:
                print("Wrong answer\nGame Over!")
                exit()
            else:
                print("Too young, EXIT")
                exit()
        elif spA > 95:
            print("Too old")
            q = ''
            q = input("Will you Play Again? (y/n) ")
            q = q.lower()
            if q == 'y':
                continue
            elif q == 'n':
                print("Thank's to take apart\nGood Bye!\nGame Over")
                exit()
            elif q == 'n':
                print("Thank's to take apart\nGood Bye!\nGame Over")
                exit()
            elif len(q) >= 2:
                print("Wrong answer.\nGame Over!")
                exit()  
            else:
                print("Too old, EXIT")
                exit()
        break
    except ValueError:
        print("Come on Enter only numbers")
        continue

cls()

print("So we have " + fpN + ", who is " + str(fpa) + " years old, and " + str(fph) + " cm tall.")
print("And we have " + spN + ", who is " + str(spA) + " years old, and " + str(sph) + " cm tall.")

print("\nHere is how I figure out your scores:\nYour age plus five times your height\n")

print("OK, now I calculate your scores\n...\n...\n")


'''
-------------------------------------------------------------------------------
Here is how to figure out scores:
player's age plus five times the height
-------------------------------------------------------------------------------

'''
# Calculating Scores

fpS = fpa + 5 * fph
spS = spA + 5 * sph

print(fpN + "'s Score is: --- " + str(fpS)) # Important to convert 'fpS' to a string: str(fpS)
print(spN + "'s Score is: --- " + str(spS))

# Highest score wins
if fpS > spS:
    print("The winner is... " + fpN)
elif fpS < spS:
    print("The winner is... " + spN)
else:
    print("The game is a draw.")

print("\nGAME OVER\nThank you both to take part!")






