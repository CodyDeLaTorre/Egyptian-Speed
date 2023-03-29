from utils.card import Deck
from utils.player import Player
import re

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
        self.times_to_place = 0

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
        placed_cards = []
        if self.bot_turn_tracker == True:
            print("Bots turn")
            self.times_to_place +=1
            while self.times_to_place > 0:
                placed_cards.append(self.bot.place_card())
                self.lose_check()
                self.times_to_place -= 1
        elif self.bot_turn_tracker == False:
            print("Players turn")
            self.times_to_place +=1
            while self.times_to_place > 0:
                placed_cards.append(self.player.place_card())
                self.lose_check()
                self.times_to_place -= 1
        for i in placed_cards:
            self.pot.append(i)
            self.turn_decision(i)
        
    def turn_decision(self,card):
        string_card = str(card)
        result = self.has_numbers(string_card)
        if result == True:
            self.flip_turn()
            self.game_loop()
        else:
            ace_result = self.ace_match(string_card)
            king_result = self.king_match(string_card)
            queen_result = self.queen_match(string_card)
            jack_result = self.jack_match(string_card)
            if ace_result == True:
                self.times_to_place += 3
                self.flip_turn()
                self.game_loop()
            elif king_result == True:
                self.times_to_place += 2
                self.flip_turn()
                self.game_loop()
            elif queen_result == True:
                self.times_to_place +=1
                self.flip_turn()
                self.game_loop()
            elif jack_result == True:
                self.flip_turn()
                self.game_loop()

    def lose_check(self):
        if len(self.bot.hand) == 52 or len(self.player.hand) == 0:
            print("Sorry, you lost I win")
            exit()
        elif len(self.player.hand) == 52 or len(self.bot.hand) ==0:
            print("NICE!! YOU WON")
            exit()
        else:
            return
            
    def flip_turn(self):
        if self.bot_turn_tracker == True:
            self.bot_turn_tracker = False
        elif self.bot_turn_tracker == False:
            self.bot_turn_tracker = True

    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)
    
    def ace_match(self,inputString):
        return bool(re.search("Ace", inputString))

    def king_match(self,inputString):
        return bool(re.search("King", inputString))

    def queen_match(self,inputString):
        return bool(re.search("Queen", inputString))

    def jack_match(self,inputString):
        return bool(re.search("Jack", inputString))
    

if __name__ == "__main__":
    game = Game()
