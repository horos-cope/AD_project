from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QDialog

from yacht import Yacht
from roll import Roll
from score import Score

class YachtDice(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.diceMainLayout = QGridLayout()

        self.diceLayout = QGridLayout()

        self.diceWindow = []
        self.diceFont = []
        self.diceButton = []

        self.newGameButton = QToolButton()
        self.newGameButton.setText('New')
        self.newGameButton.setMaximumWidth(60)
        self.newGameButton.setMaximumHeight(60)
        self.newGameButton.clicked.connect(self.startGame)
        self.diceMainLayout.addWidget(self.newGameButton, 0, 0)

        for i in range (5):
            dice = QTextEdit()
            dice.setReadOnly(True)
            dice.setAlignment(Qt.AlignCenter)
            dice.setMaximumHeight(80)
            dice.setMaximumWidth(80)
            font = dice.font()
            font.setFamily('Courier New')
            dice.setFont(font)

            fixButton = QToolButton()
            fixButton.setMaximumWidth(80)
            fixButton.setText('Fix'+(str)(i+1))
            fixButton.clicked.connect(self.fixClicked)

            self.diceWindow.append(dice)
            self.diceFont.append(font)
            self.diceButton.append(fixButton)

            self.diceLayout.addWidget(self.diceWindow[i], 1, i)
            self.diceLayout.addWidget(self.diceButton[i], 2, i)

        self.diceMainLayout.addLayout(self.diceLayout, 1, 0)


        self.rollLayout = QGridLayout()

        self.remainRoll = QTextEdit()
        self.remainRoll.setMaximumWidth(240)
        self.remainRoll.setMaximumHeight(40)
        self.remainRoll.setReadOnly(True)

        self.rollButton = QToolButton()
        self.rollButton.setMaximumWidth(160)
        self.rollButton.setMaximumHeight(40)
        self.rollButton.setText('Roll')
        self.rollButton.clicked.connect(self.rollClicked)

        self.rollLayout.addWidget(self.remainRoll, 0, 0)
        self.rollLayout.addWidget(self.rollButton, 0, 1)

        self.diceMainLayout.addLayout(self.rollLayout, 2, 0)


        #Socre
        self.scoreLayout = QGridLayout()

        self.turnPlayerLayout = QGridLayout()
        self.selectButtonLayout = QGridLayout()
        self.kindScoreLayout = QGridLayout()
        self.subtotalScoreLayout = QGridLayout()
        self.mixScoreLayout = QGridLayout()
        self.totalScoreLayout = QGridLayout()

        self.scoreTypeButton = []
        self.playerScore = []
        self.player1Score = []
        self.player2Score = []
        self.selectButton = []

        self.ScoreGroups = {
            'kind': {'name': Yacht.textKind, 'location': 0, 'layout':self.kindScoreLayout},
            'subtotal': {'name': Yacht.textSubtotal, 'location': 6, 'layout':self.subtotalScoreLayout},
            'mix': {'name': Yacht.textMix, 'location': 8, 'layout':self.mixScoreLayout},
            'total': {'name': Yacht.textTotal, 'location': 14, 'layout':self.totalScoreLayout}
        }


        self.turnText = QTextEdit()
        self.turnText.setText("Turn 1/12")
        self.turnText.setAlignment(Qt.AlignCenter)
        self.turnText.setReadOnly(True)
        self.turnText.setMaximumWidth(120)
        self.turnText.setMaximumHeight(80)
        self.turnPlayerLayout.addWidget(self.turnText, 0, 0)
        self.player1Text = QTextEdit()
        self.player1Text.setText("P1")
        self.player1Text.setAlignment(Qt.AlignCenter)
        self.player1Text.setMaximumWidth(80)
        self.player1Text.setMaximumHeight(80)
        self.turnPlayerLayout.addWidget(self.player1Text, 0, 1)
        self.player2Text = QTextEdit()
        self.player2Text.setText("P2")
        self.player2Text.setAlignment(Qt.AlignCenter)
        self.player2Text.setMaximumWidth(80)
        self.player2Text.setMaximumHeight(80)
        self.turnPlayerLayout.addWidget(self.player2Text, 0, 2)

        for group in self.ScoreGroups.keys():
            scoreList = self.ScoreGroups[group]
            for i in range(len(scoreList['name'])):
                scoreType = QToolButton()
                scoreType.setText(scoreList['name'][i])
                scoreType.setMaximumWidth(120)
                scoreType.setMaximumHeight(30)
                scoreType.clicked.connect(self.selectClicked)

                score1 = QTextEdit()
                score1.setReadOnly(True)
                score1.setMaximumWidth(80)
                score1.setMaximumHeight(30)
                score1.setStyleSheet("Color : grey")

                score2 = QTextEdit()
                score2.setReadOnly(True)
                score2.setMaximumWidth(80)
                score2.setMaximumHeight(30)
                score2.setStyleSheet("Color : grey")

                self.player1Score.append(score1)
                self.player2Score.append(score2)
                self.scoreTypeButton.append(scoreType)

                scoreList['layout'].addWidget(self.scoreTypeButton[i+scoreList['location']], i+scoreList['location'], 0)
                scoreList['layout'].addWidget(self.player1Score[i+scoreList['location']], i+scoreList['location'], 1)
                scoreList['layout'].addWidget(self.player2Score[i+scoreList['location']], i+scoreList['location'], 2)

        self.bonusExp = QLineEdit()
        self.bonusExp.setText('Bonus if Aces~Sixes are over 63 points')

        self.scoreLayout.addLayout(self.turnPlayerLayout, 0, 0)
        self.scoreLayout.addLayout(self.kindScoreLayout, 1, 0)
        self.scoreLayout.addLayout(self.subtotalScoreLayout, 2, 0)
        self.scoreLayout.addWidget(self.bonusExp, 3, 0)
        self.scoreLayout.addLayout(self.mixScoreLayout, 4, 0)
        self.scoreLayout.addLayout(self.totalScoreLayout, 5, 0)


        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(self.scoreLayout, 0, 0)
        mainLayout.addLayout(self.diceMainLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Yacht Dice')
        self.playerScore.append(self.player1Score)
        self.playerScore.append(self.player2Score)
        self.dialog = QDialog()
        self.startGame()

    def startGame(self):
        self.roll = Roll()
        self.score = Score()
        self.score.clearScore()
        self.currentPlayer = 1
        self.currentTurn = 1
        self.clearDisplay(0)
        self.clearDisplay(1)
        self.remainRoll.setText('3')
        self.roll.clearRollCount()
        self.rollButton.setEnabled(True)
        self.buttonSetting()
        self.currentPlayer = 0
        self.colorSetting(0)
        self.scoreTypeClear()

    def rollClicked(self):
        self.clearDisplay(self.currentPlayer)
        self.roll.decreaseRoll()
        numList = self.roll.diceRoll()
        
        for i in range(5):
            self.diceWindow[i].setText((str)(numList[i]))
        if self.roll.getRollCount() == 0:
            self.rollButton.setEnabled(False)

        self.display(self.score.calcScore(numList, self.currentPlayer))

    def selectClicked(self):
        self.roll.clearRollCount()
        self.rollButton.setEnabled(True)
        buttonLocation = Yacht.allYacht[self.sender().text()]
        self.score.saveScore(buttonLocation,self.currentPlayer)
        self.anotherTurnDisplay()
        self.buttonSetting()
        self.clearDisplay(self.currentPlayer)
        self.colorClear(self.currentPlayer)
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0
            self.currentTurn += 1
            self.turnText.setText('Turn '+(str)(self.currentTurn)+'/12')
            if self.currentTurn == 13:
                self.dialog_open()

        self.colorSetting(self.currentPlayer)
        self.scoreTypeSetting()


    def fixClicked(self):
        button = self.sender()
        buttonText = button.text()
        if len(buttonText) == 4:
            button.setText('Fixed'+buttonText[3])
            self.roll.fixDice((int)(buttonText[3]))
        
        else:
            button.setText('Fix'+buttonText[5])
            self.roll.unFixDice((int)(buttonText[5]))

    def clearDisplay(self, player):
        for i in range(15):
            if self.score.selectScore[player][i] != -1:
                continue
            self.playerScore[player][i].clear()
        for i in range(5):
            self.diceWindow[i].clear()

    def buttonSetting(self):
        self.roll.clearDice()
        for i in range(5):
            self.diceButton[i].setText('Fix'+(str)(i))

    def anotherTurnDisplay(self):
        for i in range(15):
            if self.score.selectScore[self.currentPlayer][i] != -1:
                self.playerScore[self.currentPlayer][i].setText((str)(self.score.selectScore[self.currentPlayer][i]))
        self.remainRoll.setText((str)(self.roll.getRollCount()))

    def display(self, scoreList):
        for i in range(15):
            self.playerScore[self.currentPlayer][i].setText((str)(scoreList[i]))
        self.remainRoll.setText((str)(self.roll.getRollCount()))

    def colorSetting(self, player):
        for i in range(15):
            textColor = 'grey'
            if self.score.selectScore[player][i] != -1:
                textColor = 'black'
            self.playerScore[player][i].setStyleSheet('Color:'+textColor+';background:yellow')

    def colorClear(self,player):
        for i in range(15):
            self.playerScore[player][i].setStyleSheet('Color:black')

    def scoreTypeClear(self):
        for group in self.ScoreGroups.keys():
            scoreList = self.ScoreGroups[group]
            for i in range(len(scoreList['name'])):
                if scoreList['name'] == Yacht.textSubtotal or scoreList['name'] == Yacht.textTotal:
                    self.scoreTypeButton[i+scoreList['location']].setEnabled(False)
                else:
                    self.scoreTypeButton[i+scoreList['location']].setEnabled(True)

    def scoreTypeSetting(self):
        for group in self.ScoreGroups.keys():
            scoreList = self.ScoreGroups[group]
            if scoreList['name'] == Yacht.textSubtotal or scoreList['name'] == Yacht.textTotal:
                continue
            for i in range(len(scoreList['name'])):
                if self.score.selectScore[self.currentPlayer][i+scoreList['location']] != -1:
                    self.scoreTypeButton[i+scoreList['location']].setEnabled(False)
                else:
                    self.scoreTypeButton[i+scoreList['location']].setEnabled(True)
                    
    def dialog_open(self):
        text = ''
        if self.score.selectScore[0][14] > self.score.selectScore[1][14]:
            text = self.player1Text.toPlainText()+' is winner'
        elif self.score.selectScore[0][14] < self.score.selectScore[1][14]:
            text = self.player2Text.toPlainText()+' is winner'
        else:
            text = 'draw'
        winnerDialog = QTextEdit(text, self.dialog)
        winnerDialog.move(0,0)
        #winnerDialog.setText(text)

        self.dialog.setWindowTitle('Winner')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(300, 200)
        self.dialog.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = YachtDice()
    game.show()
    sys.exit(app.exec_())


