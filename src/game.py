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

        self.update_hand("player", self.draw_card())
        self.update_hand("dealer", self.draw_card())

        print("player:", sum(self.playerHand))
        print("dealer:", sum(self.dealerHand))
        print("penis")
        
        playing = True

        while playing:
            choice = input("Hit or Stand: ")
            if choice == "Hit":
                self.update_hand("player", self.draw_card())
                print(sum(self.playerHand))
                if sum(self.playerHand) > 21:
                    print("Bust")
                    print("Dealer wins")
                    playing = False
                    break
            elif choice == "Stand":
                for _ in range(2):
                    time.sleep(0.5)
                    self.update_hand("dealer", self.draw_card())
                    print("dealer:", sum(self.dealerHand))
                    if sum(self.dealerHand) == 17:
                        playing = False
                        break
                    elif sum(self.dealerHand) > 21:
                        print("Bust")
                        print("Player wins")
                        playing = False
                        break
                    elif sum(self.dealerHand) == 21:
                        print("Blackjack")
                        playing = False
                        break


        if sum(self.dealerHand) > sum(self.playerHand):
            print("Dealer wins")
        elif sum(self.dealerHand) < sum(self.playerHand):
            print("Player wins")
        elif sum(self.dealerHand) == sum(self.playerHand):
            print("Push!")


if __name__ == "__main__":
    game = Blackjack()
    game.start()
    