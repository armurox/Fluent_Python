from collections import namedtuple

NUMBER_OF_SUITS = 4

Card = namedtuple('Card', ['value', 'suit'])

class FrenchDeck:
    values = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'hearts', 'clubs', 'diamonds']
    
    def __init__(self):
        self._cards = [Card(value, suit) for suit in self.suits
                                         for value in self.values]  # second one loops first, so suits will freeze, and it will go through the values
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value
        

def spades_high(card):
    suit_order = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    return FrenchDeck.values.index(card.value) * NUMBER_OF_SUITS + suit_order[card.suit]

deck = FrenchDeck()
print('Spades High!')
for card in sorted(deck, key=spades_high):
    print(card)

print('Hearts high!')
# hearts high
for card in sorted(deck, key=lambda card : FrenchDeck.values.index(card.value) * NUMBER_OF_SUITS + dict(hearts=3, diamonds=2, spades=1, clubs=0).get(card.suit)):
    print(card)

from random import shuffle

shuffle(deck)  # works because of __setitem__, would get an error otherwise
