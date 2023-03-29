import re

def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

print(has_numbers("Ace 10 of Spades"))


def king_match(inputString):
        # pattern = r"/\bKing\b/g"
        return bool(re.search("King", inputString))

print(king_match("King of Spades"))
