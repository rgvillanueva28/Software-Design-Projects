
from player import Player
from pile import Pile
from card import Card
from cardDeck import CardDeck

class Game:

	def __init__(self):
		p1 = Player(None)
		p2 = Player(None)
		self.__p1 = p1
		self.__p2 = p2

	def play(self):
		cd = CardDeck()
		cd.shuffle()

		self.__p1 = Player('Ernie')
		self.__p2 = Player('Bart')

		while(cd.getSize() >= 2):
			self.__p1.collectCard(cd.deal())
			self.__p2.collectCard(cd.deal())

		self.__p1.useWonPile()
		self.__p2.useWonPile()
		down = Pile()

		for t in range(1, 101):
			if(not(self.enoughCards(1))): break

			c1 = Card(None,None)
			c2 = Card(None,None)

			c1 = self.__p1.playCard()
			c2 = self.__p2.playCard()

			print("\nTurn ", t, ":")
			print(self.__p1.getName() ,": ", c1, " ")
			print(self.__p2.getName() ,": ", c2, " ")

			if(c1.compareTo(c2) > 0):
				self.__p1.collectCard(c1)
				self.__p1.collectCard(c2)
			elif(c1.compareTo(c2) < 0):
				self.__p2.collectCard(c1)
				self.__p2.collectCard(c2)
			else:
				down.clear()
				down.addCard(c1)
				down.addCard(c2)
				done = False

				while(not(done)):
					num = c1.getRank()

					if(not(self.enoughCards(num))): break

					print("\nWar! Players put down ")
					print(num , " cards(s).")

					for i in range(1, num+1):
						c1 = self.__p1.playCard()
						c2 = self.__p2.playCard()

					print(self.__p1.getName(), ": ", c1, " ")
					print(self.__p2.getName(), ": ", c2, " ")

					if(c1.compareTo(c2) > 0):
						self.__p1.collectCards(down)
						done = True
					elif(c1.compareTo(c2) < 0):
						self.__p2.collectCards(down)
						done = True

			print(self.__p1.numCards(), " to ", self.__p2.numCards())

	def enoughCards(self, n):
		if(self.__p1.numCards() < n or self.__p2.numCards() < n):
			return False
		return True

	def getWinner(self):
		if(self.__p1.numCards() > self.__p2.numCards()):
			return self.__p1
		elif(self.__p2.numCards() > self.__p1.numCards()):
			return self.__p2
		else:
			return None