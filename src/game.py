import random
import time
from colors import red, green
import sys

class Blackjack:
    def __init__(self):
        self.cardDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
        self.playerHand = [2,2]
        self.dealerHand = []

    def shuffle_cards(self):
        random.shuffle(self.cardDeck)

    def draw_card(self):
        return random.choice(self.cardDeck)


    def update_hand(self, turn, card):
        if turn == "player":
            self.playerHand.append(card)
        elif turn == "dealer":
            self.dealerHand.append(card)

    def get_player_hand(self):
        return sum(self.playerHand)
    
    def get_dealer_hand(self):
        return sum(self.dealerHand)

    def is_bust(self, score):
        return score > 21

    def is_blackjack(self, score):
        return score == 21

    def get_winner(self, playerScore, dealerScore):
        if playerScore > dealerScore:
            return "player"
        elif dealerScore > playerScore:
            return "dealer"

    def is_split(self):
        hand = self.playerHand
        if len(hand) == 2 and hand[0] == hand[1]:
            return True
        else:
            return False

    def split_cards(self):
        hand = {1: [self.playerHand[0]], 2: [self.playerHand[1]]}
        return hand

    def play_split(self):
        hand = self.split_cards()
        print("{0}, {1}".format(sum(hand[1]), sum(hand[2])))
        active = hand[1]
        total = sum([x + y for x, y in zip(hand[1], hand[2])])


        while total < 21:
            choice = input("Hit or Stand (split): ").lower()
            if choice == "hit":
                card = self.draw_card()
                active.append(card)
                print("{0}, {1}".format(sum(hand[1]), sum(hand[2])))
                if self.is_bust(sum(active)):
                    print("Bust")
                    print(red(str(sum(active))))
                    if active == hand[2]:
                        return
                    else:
                        active = hand[2]
                if self.is_blackjack(sum(active)):
                    print("Blackjack!")
            elif choice == "stand":
                if active == hand[2]:
                    print("{0}, {1}".format(sum(hand[1]), sum(hand[2])))
                    return
                else:
                    active = hand[2]

    def ask_split(self):
        doSplit = input("Do you want to split: ").lower()
        if doSplit == "yes":
            self.play_split()
        elif doSplit == "no":
            return False
        else:
            self.ask_split()


    def player_turn(self):
        playerSum = self.get_player_hand
        while playerSum() < 21:
            if self.is_split():
                self.ask_split()
            else:
                choice = input("hit or stand: ").lower()
                if choice == "hit":
                    self.update_hand("player", self.draw_card())
                    print(f"Player: {playerSum()}")
                    if self.is_bust(playerSum()):
                        print("Player Bust")
                        print("Dealer wins")
                        return sys.exit(1)
                    elif self.is_blackjack(playerSum()):
                        print("Player hit blackjack")
                elif choice == "stand":
                    return False

    def dealer_turn(self):
        dealerSum = self.get_dealer_hand
        while dealerSum() < 17:
            time.sleep(0.5)
            self.update_hand("dealer", self.draw_card())
            print("dealer:", dealerSum())
            if self.is_bust(dealerSum()):
                print("Dealer Bust")
                return sys.exit(1)
            elif self.is_blackjack(dealerSum()):
                print("Dealer hit blackjack")
        return


    def start(self):
        self.shuffle_cards()

        dealerSum = self.get_dealer_hand
        playerSum = self.get_player_hand

        self.update_hand("player", self.draw_card())
        self.update_hand("dealer", self.draw_card())

        print("player:", playerSum())
        print("dealer:", dealerSum())
        
        self.player_turn()
        self.dealer_turn()

        winner = self.get_winner(playerSum(), dealerSum())
        if winner == None:
            print("Push! No winner")
        elif winner:
            print(f"{winner} wins!")


if __name__ == "__main__":
    game = Blackjack()
    game.start()
    