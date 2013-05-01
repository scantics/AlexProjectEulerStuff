#each hand to be represented by an array giving the card value of each possible
#hand, zero if that hand is not in the hand
class PokerHand:
    vals = enumerate(['1','2','3','4','5','6','7','8','9','10','J','Q','K','A'])
    hands = enumerate(['highCard', 'onePair', 'twoPair', 'threeOfAKind',
                       'straight', 'flush', 'fullHouse', 'fourOfAKind',
                       'straightFlush', 'royalFlush'])
    

    
    def __init__(self, handStr):
        self.handVals  = [0]*10
        self.handFlags = [False]*5 #True if card is used in a hand 
        self.cardStrList = handStr.split(' ')
        self.hand = [(0,0)]*5
        for i in range(5):
            hand[i][0] = cardStrList[i][0:len(cardStrList[i])-1]
            hand[i][1] = sardStrList[i][len(cardStrList[i])-1]

        
        self.checkHand()
        
        
    def checkHand():
        pair = self.checkPair
        if pair > 0:
            if self.TwoPair
    
    def checkHighCard():
        maxVal = 0
        for i, card in self.hand:
            if self.handFlags[i]: continue
            if vals[card[0]] < maxVal:
                maxVal = vals[card[0]]
        return maxVal


    def checkPair():
        pair = 0
        for i in range(4):
            first = self.hand[i][0]
            for j in range(i+1,5):
                if first == self.hand[j][0]:
                    pair = vals[first]
        if pair > 0:
            self.handVals[1] = pair
            self.checkTwoPair()
            self.checkThreeAndFourOfAKind(pair)
        return pair

    def checkTwoPair():
        firstPair = self.handVals[1]
        if firstPair == 0: return 0
        for i in range(4):
            first = self.hand[i][0]
            if firstPair != first:
                for j in range(i+1,5):
                    if first == self.hand[j][0]:
                        secPair = vals[first]
        if secPair > 0:
            if secPair > firstPair:
                self.handVals[2] = secPair
            else:
                self.handVals[2] = firstPair
        return


    def checkThreeAndFourOfAKind(pair):
        for i in range(5):
            if vals[self.hand[i][0]] == pair:
                count += 1
        if count >= 3:
            self.handVals[3] = pair
            if count == 4:
                self.handVals[7] = trip
        return














        
