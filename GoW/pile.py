#Bob Caridad

class Pile:
    def _init_(self, r, s):
        self._rank = r
        self._suit = s

    def getRank(self):
        return self._rank
    
    def getSuit(self):
        return self._suit
    
    def compareTo(self, ob):
        other = Pile(ob._rank, ob._suit)
        selfRank = self.getRank()
        otherRank = other.getRank()
        if(selfRank == 1): selfRank = 14
        if(otherRank == 1): otherRank = 14
        return selfRank - otherRank

    def _eq_(self, ob):
        if(isinstance(ob,Pile)):
            other = Pile(ob._rank, ob._suit)
            return self._rank == other._rank and self._suit == other._suit
        else:
            return false

    def _str_(self):
        suitList = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
        if(self._ranl == 1): val = "Ace"
        elif(self._rank == 11): val = "Jack"
        elif(self._rank == 12): val = "Queen"
        elif(self._rank == 13): val = "King"
        else: val = str(self._rank)
        s = val + " of " + suitList[self._suit]
        return s
