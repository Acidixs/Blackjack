import random


class Blackjack:
    def __init__(self):
        self.cardDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
        self.playerHand = []
        self.dealerHand = []

    def shuffle_cards(self):
        random.shuffle(self.cardDeck)

    def draw_card(self):
        card = random.choice(self.cardDeck)
        self.cardDeck.pop(card)
        return card

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

        print(self.playerHand)
        print(self.dealerHand)
        

        while True:
            choice = input("Hit or Stand: ")
            if choice == "Hit":
                self.draw_card("player")
                print("player:", p)
                if p > 21:
                    print("Bust")
                    break


if __name__ == "__main__":
    game = Blackjack()
    game.start()
    