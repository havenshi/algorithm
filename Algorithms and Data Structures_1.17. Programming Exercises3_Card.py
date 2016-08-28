# 14.Design a class to represent a playing card. Now design a class to represent a deck of cards. Using these two classes, implement a favorite card game.
import random

class Card:
	# properties
	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
	rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	# two attributes of suit and rank number
	def __init__(self, suit=0, rank=1):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	def __cmp__(self, other):
		# compare by suit, then rank.
		
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		
		return cmp(t1, t2)

card1=Card()
card2=Card(2,8)
card3=Card(2,3)
print card1                 # Ace of Clubs
print card1.__cmp__(card2)  # -1
print card2.__cmp__(card3)  # 1


class Deck:
	# attributes of cards(list)
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
	
	def __str__(self):
		s = ''
		for i in range(len(self.cards)):
			s += " " * i + str(self.cards[i]) + "\n"
		return s
		
	
	# basic methods
	def add_card(self, card):
		self.cards.append(card)

	def remove_card(self, card):
		self.cards.remove(card)

	def pop_card(self, i=-1):
		return self.cards.pop(i)

	def sort(self):
		self.cards.sort()

	def move_cards(self, hand, num):        # hand a card
		for i in range(num):
			hand.add_card(self.pop_card())
			
			
	def shuffle(self):
		rng = random.Random()        # Create a random generator
		for i in range(len(self.cards)):
			j = rng.randrange(i, len(self.cards))
			(self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i]) # each card change with the cards before it





class Hand(Deck):
	# inheritance
	def __init__(self,name):
		self.name=name
		self.cards = []

	def __str__(self):
		h = ''
		for i in range(len(self.cards)):
			h += " " * i + str(self.cards[i]) + "\n"
		return self.name + ' has cards of: '+ '\n'+ h


if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()

	hand = Hand('bob')

	deck.move_cards(hand,5)
	
	print hand
