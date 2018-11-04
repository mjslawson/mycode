#!/usr/bin/env python3

"""
Author: mjslawson

This program asks a user to complete the movie title
"""

def main():
    """ Main Program """
    rounding = 0           # integer round initiated to 0
    while True:        # sets up an infinite loop condition
        rounding = rounding + 1     # increase the round counter
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input()    # string answer collected from user
        if answer.lower() == 'brian': # logic to check if user gave correct answer
            print('Correct!')
            break             # break statement escapes the while loop
        elif answer.lower() == 'shrubbery': # setec astronomy
            print('You gave the super secret answer!')
            break
        elif rounding == 3:    # logic to ensure round has not yet reached 3
            print('Sorry, the answer was Brian.')
            break             # break statement escapes the while loop
        else:                 # if answer was wrong, and round is not yet equal to 3
            print('Sorry. Try again!')

main()
