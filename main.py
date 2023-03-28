from utils.card import Deck
from utils.player import Player

# rules: 
# You win by ending up with the whole deck
# You always split the deck evenly between players
# cant see you cards values
# each player puts down a card one at a time 
# if number card put down one card and keep going
# if jack put down one card then give all cards to player who put down the face card
# if queen put down two cards then give all cards to player who put down the face card
# if king put down three cards then give all cards to player who put down the face card
# if ace put down four cards then give all cards to player who put down the face card
# if another player puts a face card down while putting down their required amount it switches to the next personCody
 

class Game():
    def __init__(self):
        self.bot_turn_tracker = True
        self.pot = []
        self.deck = Deck()
        self.bot = Player('bot')
        self.player = Player('player')

        self.intro()
        self.game_loop()

    def intro(self):
        print(f"bot: alright {self.player.name} let's begin")
        print("bot: I'm going to shuffle and split the deck for us")
        self.deck.shuffle()
        split_deck = self.deck.split()
        self.player.hand = split_deck[0]
        self.bot.hand = split_deck[1]
        print("----The bot hands you your deck-----")
        print("bot: I'll start")

    def game_loop(self):
        if self.bot_turn_tracker == True:
            placed_card = self.bot.place_card()
        elif self.bot_turn_tracker == False:
            placed_card = self.player.place_card()
        self.pot.append(placed_card)
        # print(placed_card)
        self.turn_decision(placed_card)
        print(self.pot)
        
    def turn_decision(self,card):
        str(card)
        print(type(card))
        print(card)
        result = self.has_numbers(card)
        if result == True:
            self.flip_turn()
    
    def flip_turn(self):
        if self.bot_turn_tracker == True:
            self.bot_turn_tracker = False
        else:
            self.bot_turn_tracker = True

    def has_numbers(inputString):
        return bool(char.isdigit() for char in inputString)



if __name__ == "__main__":
    game = Game()
