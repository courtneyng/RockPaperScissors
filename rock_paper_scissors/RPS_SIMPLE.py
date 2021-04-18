# Program ID: rock_paper_scissors_simplified
# Author: Courtney Ng
# Period: 7
# Program Description: Writing a program to simulate the game rock paper scissors.

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
            if x == answer:
                print ("It's a tie.")
                print ("No winners.")