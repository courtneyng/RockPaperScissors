# Program ID: rock_paper_scissors_simplified
# Author: Courtney Ng
# Period: 7
# Program Description: Writing a program to simulate the game rock paper scissors.

# line provides rand number functionality
# from random import *
# x = randint (1, 3)
# print ("Random Integer: ", x)

ans = input("Do you want to play Rock-Paper-Scissors?")
yes = "yes"
no = "no"
rock = 1
paper = 2
scissors = 3

while ans != no:
        if ans != yes:
            print ("Okay.")
        else:
            print ("Let's play.")
            answer = int(input("Choose 1 for rock, 2 for paper, and 3 for scissors."))
            from random import *                    # calls for random integer
            x = randint (1, 3)
            print ("Random Integer: ", x)
            print ("Your answer:", answer)
            if x == answer:                     # handles all of the tie statements
                print ("It's a tie.")
                print ("No winners.")
            else:
                if x == rock:                   # all of the rock (CPU) vs Player input
                    if answer == paper:
                        print ("You win!")
                        print ("CPU loses.")
                    else:
                        answer == scissors
                        print ("You lose.")
                        print ("CPU wins!")
                else:
                    if x == paper:               # all of the paper (CPU) vs Player input
                        if answer == rock:
                            print ("You lose.")
                            print ("CPU wins!")
                        else:
                            answer == scissors
                            print ("You win!")
                            print ("CPU loses.")
                    else:
                        x == scissors               # all of the scissors (CPU) vs Player input
                        if answer == rock:
                            print ("You win!")
                            print ("CPU loses.")
                        else:
                             answer == paper
                             print ("You lose.")
                             print ("CPU wins!")
        ans = input("Play again?")                   # can be in the loop