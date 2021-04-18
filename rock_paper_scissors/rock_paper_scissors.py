# Program ID: rock_paper_scissors
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
            from random import *
            x = randint (1, 3)
            print ("Random Integer: ", x)
            print ("Your answer:", answer)
            if x < paper: # rock
                if answer < paper: # rock vs rock
                    print ("It's a tie.")
                    print ("No winners.")
                    ans = input("Play again?")
                else:
                    if rock < answer < scissors: # rock vs paper
                        print ("You win!")
                        print ("CPU loses.")
                        ans = input("Play again?")
                    else:
                        answer > paper # rock vs scissors
                        print ("You lose.")
                        print ("CPU wins")
                        ans = input("Play again?")
            else:
                if rock < x < scissors: # paper
                    if answer < paper: # paper vs rock
                        print ("You lose.")
                        print ("CPU wins.")
                        ans = input("Play again?")
                    else:
                        if rock < answer < scissors: # paper vs paper
                            print ("It's a tie.")
                            print ("No winners.")
                            ans = input("Play again?")
                        else:
                            answer > paper # paper vs scissors
                            print ("You win!")
                            print ("CPU loses.")
                            ans = input("Play again?")
                else:
                    if answer < paper: # scissors vs rock
                        print ("You win!")
                        print ("CPU loses.")
                        ans = input ("Play again?")
                    else:
                        if rock < answer < scissors: # scissors vs paper
                            print ("You lose.")
                            print ("CPU wins.")
                            ans = input("Play again?")
                        else:
                            answer > paper # scissors vs scissors
                            print ("It's a tie.")
                            print ("No winners.")
                            ans = input("Play again?")