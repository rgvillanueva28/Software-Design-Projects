from pile import Pile

class Player:

    def __init__(self, n):
        self.__name = n
        self.__playPile = Pile()
        self.__wonPile = Pile()

    def playCard(self):
        if(self.__playPile.getSize() == 0):
            self.useWonPile()
        if(self.__playPile.getSize() > 0):
            return self.__playPile.nextCard()
        return None

    def getName(self):
        return self.__name

    def collectCard(self, c):
        self.__wonPile.addCard(c)

    def collectCards(self, p):
        self.__wonPile.addCards(p)

    def useWonPile(self):
        self.__playPile.clear()
        self.__playPile.addCards(self.__wonPile)
        self.__wonPile.clear()

    def numCards(self):
        return self.__playPile.getSize() + self.__wonPile.getSize()