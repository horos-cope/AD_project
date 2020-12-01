import random

class Roll:
    
    def __init__(self):
        self.fixCheck = [False,False,False,False,False]
        self.currentDice = [0, 0, 0, 0, 0]
        self.rollCount = 3

    def diceRoll(self):
        for i in range(5):
            if not self.fixCheck[i]:
                self.currentDice[i] = random.randrange(6)+1
                
        return self.currentDice
    
    def fixDice(self, num):
        self.fixCheck[num] = True
        
    def unFixDice(self, num):
        self.fixCheck[num] = False
        
    def clearDice(self):
        self.fixCheck = [False,False,False,False,False]
    
    def decreaseRoll(self):
        self.rollCount  -= 1
        
    def getRollCount(self):
        return self.rollCount
    
    def clearRollCount(self):
        self.rollCount = 3
        