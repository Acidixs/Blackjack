import random
import time

class Blackjack:
    def __init__(self):
        self.cardDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
        self.playerHand = []
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

    def bust(self, score):
        return score > 21

    def hit_blackjack(self, score):
        return score == 21

    def start(self):
        self.shuffle_cards()

        dealerSum = self.get_dealer_hand
        playerSum = self.get_player_hand

        self.update_hand("player", self.draw_card())
        self.update_hand("dealer", self.draw_card())

        print("player:", playerSum())
        print("dealer:", dealerSum())
        
        playing = True

        while playing:
            choice = input("Hit or Stand: ")
            if choice == "Hit":
                self.update_hand("player", self.draw_card())
                print(playerSum())
                if self.bust(playerSum()):
                    print("Bust")
                    print("Dealer wins")
                    playing = False
                    break
                elif self.hit_blackjack(playerSum()):
                    print("Player hit blackjack")

            elif choice == "Stand":
                while dealerSum() < 17:
                    time.sleep(0.5)
                    self.update_hand("dealer", self.draw_card())
                    print("dealer:", dealerSum())
                    if self.bust(dealerSum()):
                        print("Bust")
                        playing = False
                        break
                    elif self.hit_blackjack(dealerSum()):
                        print("Dealer hit blackjack")



if __name__ == "__main__":
    game = Blackjack()
    game.start()
    