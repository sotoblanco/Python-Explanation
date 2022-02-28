# card class

# SUIT, RANK, VALUE, 

# DECK 

# PLAYER
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


two_hearts = Card("Hearts", "Two")

print(two_hearts)

three_of_clubs = Card("Clubs", "Three")

two_hearts.suit
two_hearts.rank

values[two_hearts.rank]

print(two_hearts.value < three_of_clubs.value)
