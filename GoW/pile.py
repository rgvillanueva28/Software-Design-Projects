#Bob Caridad

class Pile:

	def __init__(self):
		self.__pile = [None] * 52
		self.__front = 0
		self.__end = 0

	def getSize(self):
		return self.__end - self.__front
        
	def clear(self):
		self.__front = 0
		self.__end = 0

	def addCard(self, c):
		self.__pile[self.__end] = c
		self.__end += 1
		return c

	def addCards(self, p):
		while(p.getSize() > 0):
			self.addCard(p.nextCard())

	def nextCard(self):
		if(self.__front == self.__end):
			return None
		c = self.__pile[self.__front]
		self.__front += 1
		return c
	
	def display(self):
		for i in range(0, self.__end):
			print(self.__pile[i], end = " ")