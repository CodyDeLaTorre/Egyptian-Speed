from .card import Card, Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def place_card(self):
        return self.hand.pop().show()
