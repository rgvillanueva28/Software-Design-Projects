#clint Valencia
class Card:
	def __init__(self, r, s):
		self.rank = r
		self.suit = s
	def getRank(self):
		return self.rank
	def getSuit(self):
		return self.suit
	def compareTo(self, ob):	
		other = Card(ob.rank, ob.suit)	
		selfRank = self.getRank()
		otherRank = other.getRank()
		if(selfRank == 1): selfRank = 14
		if(otherRank == 1): otherRank = 14
		return selfRank - otherRank
	def __eq__(self, ob):
		if(isinstance(ob,Card)):
			other = Card(ob.__rank, ob.__suit)
			return self.rank == other.__rank and self.suit == other.__suit
		else:
			return false
	def __str__(self):
		suitList = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
		if(self.rank == 1): val = "Ace"
		elif(self.rank == 11): val = "Jack"
		elif(self.rank == 12): val = "Queen"
		elif(self.rank == 13): val = "King"
		else: val = str(self.rank)
		s = val  + " of " + suitList[self.suit]
		return s