#!/usr/bin/ env python3
# 04/26/2020
# @uthor Drake Greeott
# Design and implement an object-oriented program for a simple game of
# blackjack that provides for one player and a dealer (the computer).

from db import Card, Deck, Hand

#Creating the game
class Blackjack():
    def __init__(self):
        pass

    #function to display and play the game
    def play_game(self):
        print("Blackjack")
        print()

        
        game = True

        #while loop for the start of the game
        while game:
            #creating the deck variable
            self.deck = Deck()
            self.deck.shuffle_cards()

            #creating the players hand and dealers hand
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            #deal two cards to each player and dealer
            for i in range(2):
                self.player_hand.add_card(self.deck.deal_cards())
                self.dealer_hand.add_card(self.deck.deal_cards())

            #showing one card of the dealers hand and both cars of the players
            print("DEALER'S SHOW CARD:")
            self.dealer_hand.display_start()
            print()
            print("YOUR CARDS:")
            self.player_hand.display_start()
            print()
                    
            game_over = False

            #while loop for the rest of the game
            while not game_over:
                player_points = self.player_hand.get_points()
                dealer_points = self.dealer_hand.get_points()
                #determining of the player of dealer has blackjack
                blackjack_player, blackjack_dealer = self.blackjack_check()


                #if statement to determine what text should be printed to the screen
                if blackjack_player or blackjack_dealer:
                    game_over = True
                    self.show_blackjack(blackjack_player, blackjack_dealer)
                    continue

                #creating the choice variable and question to want to hit or stand                
                choice = input("Hit or stand? (hit/stand): ").lower()
                print()                
                    
                #if statment on if choice = "hit"
                if choice == "hit":
                    
                    #add a card to the players hand
                    self.player_hand.add_card(self.deck.deal_cards())

                    #display the cards on the screen
                    print("YOUR CARD'S: ")
                    self.player_hand.display_start()
                    print()

                    

                    #if statment to run the player over function
                    if self.player_over():
                        self.show_points(player_points, dealer_points)
                        print("You have busted!")
                        game_over = True

                #else if statement for choice = "stand"
                else:
                   
                    if dealer_points < 17:
                        #to check the function to see if the dealer shoud hit or stand
                        self.dealer_hand.add_card(self.deck.deal_cards())
                    elif dealer_points >= 17:

                        if self.dealer_over():
                            #to display the dealers whole hand on the screan
                            print("DEALER'S CARD'S: ")
                            self.dealer_hand.display_end()
                            self.show_points(player_points, dealer_points)
                            print("You have busted!")
                            game_over = True
                        else:
                            #to display the dealers whole hand on the screan
                            print("DEALER'S CARD'S: ")
                            self.dealer_hand.display_end()
                            self.show_points(player_points, dealer_points)
                            self.decide_winner(player_points, dealer_points)
                            game_over = True
                
                    
            #to determine of the player wants to play again
            print()
            again = input("Play Again? (y/n) ")
        
            while again.lower() not in ["y", "n"]:
                if again.lower() == "n":
                    print("Come back soon!")
                    playing = False
                else:
                    game_over = False

                        
                
    #checking for blackjack for both the player and dealer
    def blackjack_check(self):
        player = False
        dealer = False
        if self.player_hand.get_points() == 21:
            player = True
        if self.dealer_hand.get_points() == 21:
            dealer = True

        return player, dealer

    #showing the text on if either or both the player and deal have 21
    def show_blackjack(self, blackjack_player, blackjack_dealer):
        if blackjack_player and blackjack_dealer:
            print("Both players have blackjack! Draw!")

        elif blackjack_player:
            print("You have blackjack! You win!")

        elif blackjack_dealer:
            print("Dealer has blackjack! Dealer wins!")
            

    #to show the end points of both the player and dealer
    def show_points(self, player_points, dealer_points):
        print()
        print("YOUR POINTS: ", player_points)
        print("DEALER'S POINTS:", dealer_points)
        print()

    #to determine if the player wins, ties, or the dealer wins
    def decide_winner(self, player_points, dealer_points):
        if player_points > dealer_points:
            print("You Win!")
        elif player_points == dealer_points:
            print("Tie!")                                
        else:
            print("Dealer Wins!")

        game_over = True


    #to determine if the players hand is over 21
    def player_over(self):
        return self.player_hand.get_points() > 21

    #to determine if the dealers hand is over 21
    def dealer_over(self):
        return self.dealer_hand.get_points() > 21
        
