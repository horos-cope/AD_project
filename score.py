class Score:

    def __init__(self):
        self.scoreBoard = []
        self.selectScore = [[],[]]
        self.currentScore = []
        for i in range(15):
            self.scoreBoard.append(0)
            self.currentScore.append(0)
            self.selectScore[0].append(-1)
            self.selectScore[1].append(-1)
        self.selectScore[0][6] = 0
        self.selectScore[0][14] = 0
        self.selectScore[1][6] = 0
        self.selectScore[1][14] = 0
        self.flag = True

        self.ssList = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
        self.lsList = [[1,2,3,4,5],[2,3,4,5,6]]


    def calcScore(self, diceList,player):
        diceCount = [0, 0, 0, 0, 0, 0, 0]
        for i in range(8,14):
            self.currentScore[i] = 0
        for i in diceList:
            diceCount[i] += 1

        print(diceCount)

        for i in range(6):
            self.currentScore[i] = diceCount[i+1]*(i+1)
            self.currentScore[8] += self.currentScore[i]
        
        if 4 in diceCount or 5 in diceCount:
            self.currentScore[9] = self.currentScore[8]
        if 2 in diceCount and 3 in diceCount:
            self.currentScore[10] = self.currentScore[8]
        for i in self.ssList:
            for j in i:
                if not diceCount[j]:
                    break
            else:
                self.currentScore[11] = 15
                break
        for i in self.lsList:
            for j in i:
                if not diceCount[j]:
                    break
            else:
                self.currentScore[12] = 30
                break
        if 5 in diceCount:
            self.currentScore[13] = 50
        
        return self.makeScoreBoard(player)

    def saveScore(self, location, player):
        self.selectScore[player][location] = self.currentScore[location]
        if location < 6:
            self.selectScore[player][6] += self.selectScore[player][location]
            if self.selectScore[player][6] >= 63 and self.flag:
                self.flag = False
                self.selectScore[player][14] += 35
                self.selectScore[player][7] = 35
        self.selectScore[player][14] += self.selectScore[player][location]
        for i in range(15):
            self.currentScore[i] = 0

    def makeScoreBoard(self, player):
        for i in range(15):
            if self.selectScore[player][i] != -1:
                self.scoreBoard[i] = self.selectScore[player][i]
            else:
                self.scoreBoard[i] = self.currentScore[i]
        return self.scoreBoard
    
    def clearScore(self):
        for i in range(15):
            self.selectScore[0][i] = -1
            self.selectScore[1][i] = -1