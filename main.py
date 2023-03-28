from utils.card import Card, Deck
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
 
def game():
    pot = []
    deck = Deck()
    #intro
    # deck.show()
    name = input("whats your name?: ")
    player = Player(name)
    print(f"alright {player.name} let's begin")
    print("I am going to shuffle and split the deck for us")
    deck.shuffle()
    split_deck = deck.split()
    player.hand = split_deck[0]
    
    # print(player.showHand())
    print(player.draw_card())


if __name__ == "__main__":
    game()
