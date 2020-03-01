print("try player")

class Player():
    def __init__(self, n):
        self.name = n
        self.playPile = new Pile()
        self.wonPile = new Pile()

    Card playCard():
        if (playPile.getSize() == 0):
            useWonPile()
        if (playPile().getSize > 0):
            return playPile.nextCard()
        return None

    def getName(self):
        return self.name

    def collectCard(self, Card c):
        self.wonPile.addCard(c)

    def collectCard(self, Pile p):
        self.wonPile.addCard(p)

    def useWonPile(self):
        playPile.clear()
        playPile.addCard(wonPile)
        wonPile.clear()

    def numCard(self);
        return playPile.getSize() + wonPile.getSize()