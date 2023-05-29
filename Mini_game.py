import random
import os
import re

while (1<2):

    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")


    userChoice = input("Choose your weapon [R]ock, [P]aper, [S]cissors, [E]xit: ")


    if (not re.match("[SsRrPpEe]", userChoice)) or (len(userChoice) != 1):
        print("Please choose a letter:")
        print("[R]ock, [P]aper, [S]cissors, [E]xit")
        continue

    print ("You chose: " + userChoice)


    if (userChoice == 'E' or userChoice == 'e' ):
        print('Exiting Game..')
        break

    choices = ['R', 'P', 'S']

    opponenetChoice = random.choice(choices)

    print("I chose: " + opponenetChoice)

    if opponenetChoice == str.upper(userChoice):
        print ("Tie! ")

    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print ("Scissor beats rock, I win!")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beats rock, I win!  ")
        continue
    else:
        print ("You Win!")
