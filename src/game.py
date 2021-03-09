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
                if (playerSum()) > 21:
                    print("Bust")
                    print("Dealer wins")
                    playing = False
                    break
            elif choice == "Stand":
                for _ in range(2):
                    time.sleep(0.5)
                    self.update_hand("dealer", self.draw_card())
                    print("dealer:", dealerSum())
                    if (dealerSum()) == 17:
                        playing = False
                        break
                    elif (dealerSum()) > 21:
                        print("Bust")
                        print("Player wins")
                        playing = False
                        break
                    elif (dealerSum()) == 21:
                        print("Blackjack")
                        playing = False
                        break


if __name__ == "__main__":
    game = Blackjack()
    game.start()
    