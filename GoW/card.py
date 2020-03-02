class Card:
	def __init__(self, r, s):
		self.__rank = r
		self.__suit = s
	def getRank(self):
		return self.__rank
	def getSuit(self):
		return self.__suit
	def compareTo(self, ob):	
		other = Card(ob.__rank, ob.__suit)	
		selfRank = self.getRank()
		otherRank = other.getRank()
		if(selfRank == 1): selfRank = 14
		if(otherRank == 1): otherRank = 14
		return selfRank - otherRank
	def __eq__(self, ob):
		if(isinstance(ob,Card)):
			other = Card(ob.__rank, ob.__suit)
			return self.__rank == other.__rank and self.__suit == other.__suit
		else:
			return false
	def __str__(self):
		suitList = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
		if(self.__rank == 1): val = "Ace"
		elif(self.__rank == 11): val = "Jack"
		elif(self.__rank == 12): val = "Queen"
		elif(self.__rank == 13): val = "King"
		else: val = str(self.__rank)
		s = val  + " of " + suitList[self.__suit]
		return s