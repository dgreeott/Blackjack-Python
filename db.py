#!/usr/bin/ env python3
# 04/26/2020
# @uthor Drake Greeott
# Design and implement an object-oriented program for a simple game of
# blackjack that provides for one player and a dealer (the computer).

import random

#Creating the card class that a card belongs to a suit and has points
class Card():
    #intializing the suit and points
    def __init__(self, suit, points):
        #intializing the suit and points
        self.suit = suit
        self.points = points

    #To determine the order of points and suits when printed
    def __repr__(self):
        return " of ".join((self.points, self.suit))

#Creating the deck class that has 52 cards in a deck and will go down per draw
class Deck():
    def __init__(self):
        #intializing the cards varible with both the suits and points
        self.cards = [Card(s, p) for s in ["Spade", "Clubs", "Hearts", "Diamonds"]
                      for p in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "Jack", "Queen", "King"]]

    #to shuffle the cards 
    def shuffle_cards(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    #funtion to deal the cards
    def deal_cards(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

#Creating the hand class is to give each play cards in their hand
class Hand():
    #initializing dealer, cards, and points
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.points = 0

    #function for adding a card to the hand
    def add_card(self, card):
        self.cards.append(card)

    #function to calculate the points in a hand
    def calculate_points(self):
        self.points = 0
        ace = False
        for card in self.cards:
            if card.points.isnumeric():
                self.points += int(card.points)
            else:
                if card.points == "Ace":
                    ace = True
                    self.points += 11
                else:
                    self.points += 10

        if self.points > 21 and ace:
            self.points -= 10 

    #function to get the points
    def get_points(self):
        self.calculate_points()
        return self.points

    def dealer_hit(self):
        if self.get_points() < 17:
            self.add_card(card)
        else:
            pass

    #function to determine if the dealer should get another card
    def dealer_hit(self, card):
        if self.points < 17:
            self.cards.append(card)
        else:
            return

    #function to display one dealer card and the players cards
    def display_start(self):
        if self.dealer:
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)

    #function to display both dealers cards at end of game
    def display_end(self):
        if self.dealer:
            print(self.cards[0])
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
