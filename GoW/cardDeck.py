CardDeck: import random from card import Card

class CardDeck:

	def __init__(self):
		self.__deck = [None] * 52
		self.fill()
		self.__numCards = 52

	def shuffle(self):
		random.shuffle(self.__deck)

	def deal(self):
		if(self.__numCards == 0): return None
		self.__numCards -= 1
		return self.__deck[self.__numCards]

	def getSize(self):
		return self.__numCards

	def fill(self):
		i = 0
		for r in range(1, 14):
			for s in range(1,5):
				self.__deck[i] = Card(r, s)				
				i += 1
		self.__numCards = 52

	def test(self):
		return self.__deck[0]