import random
from datetime import datetime

class CardDeck:
    def __init__(self):
        self.cardRanks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        self.suits = ("Hearts", "Clubs", "Diamonds", "Spades")
        self.values = {"Ace": 1 ,"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" :7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10}
        self.cards = [f"{card} {suit}" for card in self.cardRanks for suit in self.suits] 

    def shuffle_cards(self):
        print("shuffling cards")
        random.shuffle(self.cards)


class CardHand(CardDeck):
    def __init__(self, name, isDealer):
        super().__init__()
        self.name = name
        self.isDealer = isDealer
        self.hand = []

    def hit(self):
        card = random.choice(self.cards)
        print(self.name, "hit", card)
        self.cards.remove(card)
        self.hand.append(card)  

    def get_value(self, card):
        rank = card.split()[0] 
        value = self.values[rank]
        return value

    def get_total(self):
        return sum(list(map(self.get_value, self.hand)))

    def show_hand(self):
        total = self.get_total()
        print(f"{self.name}: {self.hand}")
        print(f"Total: {total}")


class Game(CardHand):
    def __init__(self):
        super().__init__("name", "isDealer")
        self.winner = None
        self.playing = True

    def save_match(self, winner, playerHand, dealerHand):
        time = datetime.now().replace(microsecond=0)
        with open("logs.txt", "a+") as f:
            f.write(f"[{time}] Winner: {winner} - player hand: {playerHand} - dealer hand: {dealerHand}\n")
        
    def play(self):
        player = CardHand("Aleksander", False)
        dealer = CardHand("Mike", True)
        self.shuffle_cards()
        player.hit()
        player.show_hand()
        dealer.hit()
        dealer.show_hand()
        
        # player turn
        while True and self.playing:
            if player.get_total() > 21:
                print("Player bust")
                self.winner = dealer.name
                self.playing = False
                break
            elif player.get_total() == 21:
                print("Player hit blackjack")
            move = str(input("Hit or Stand: "))
            if move.lower() == "hit":
                player.hit()
                player.show_hand()
            elif move.lower() == "stand":
                print("breaking")
                break
        
        # dealer turn
        while dealer.get_total() < 17 and self.playing: # Dealer needs to hit up to 16
            dealer.hit()
            dealer.show_hand()

            if dealer.get_total() > 21:
                print("Dealer Bust")
                self.winner = player.name
                print("set winner to ", self.winner)
                self.playing = False
                break
            elif dealer.get_total() == 21:
                print("Dealer hit blackjack")


        if self.winner == None: # If no side has busted, see who has the largest sum
            if dealer.get_total() > player.get_total():
                self.winner = dealer.name
            elif player.get_total() > dealer.get_total():
                self.winner = player.name

        print("Game Ended!")
        dealer.show_hand()
        player.show_hand()

        print(f"Winner is {self.winner}")
        self.save_match(self.winner, player.hand, dealer.hand)

if __name__ == "__main__":
    game = Game()
    game.play()


    