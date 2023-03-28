import random
import time

names = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    
    def show(self):
        print("{} of {}".format(self.val, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in names:
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r] , self.cards[i]
        print("shuffling...")
        time.sleep(1)
    def split(self):
        print("splitting...")
        half = len(self.cards)//2
        time.sleep(1)
        return self.cards[:half], self.cards[half:]
    # def draw_card(self):
    #     return self.cards.pop()
