# What is a class?
#A class defines the methods and variables that an object will have, like class person will have name and age 

# What is an instance?
#A specific 'copy' of a class/object

# What is encapsulation?
#Bundling data and methods into a single 'capsule' to hide inner workings and protect data

# What is abstraction?
#Simplifying the code and hiding complexity

# What is inheritance?
#Creating classes based on existing ones so the new class can 'inherit' characteristics from existing classes

# What is multiple inheritance?
#Inheritance from more then one parent object/class

# What is polymorphism?
#Allows objects to have multiple forms/behaviors

# What is method resolution order or MRO?
#the sequence in which a method is searched for in a class hierarchy

#Part 2
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random
class Card():

    def __init__(self, suit,value):
        self.suit=suit
        self.value=value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck():

    def __init__(self):
        self.cards=[]
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.build_deck()

    def build_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value))
                

    def shuffle(self):
        if len(self.cards)<52:
            return (f'Deck is not complete, only {len(self.cards)} cards in deck')
        else:
            for cards in self.cards:
                print (cards)
            random.shuffle(self.cards)
            
        
    def deal(self):
        print( self.cards.pop())
        print(f'{len(self.cards)} cards remaining')

deck = Deck()
deck.shuffle()
deck.deal()



