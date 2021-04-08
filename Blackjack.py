#!/usr/bin/ env python3
# 04/26/2020
# @uthor Drake Greeott
# Design and implement an object-oriented program for a simple game of
# blackjack that provides for one player and a dealer (the computer).

from business import Blackjack

#creating the main fucntion
def main():
    #Calling classes and functions to the main to run
    blackjack = Blackjack()
    blackjack.play_game()
    
if __name__ == "__main__":
    main()
