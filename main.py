from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from BotGui import Ui_MainWindow
from _TekkenBotLauncher import TekkenBotLauncher
from BotFrameTrap import BotFrameTrap
from BotOptionsModule import BotOptions


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        # set default vars
        self.selectedPlayer = None
        self.isPunishmentOn = None
        self.stayOnTheGround = None
        self.escapeFromThrows = None
        self.blockType = None
        # Check if PunishBot is on or off
        self.updateBotOptions()
        # Check player side on bot start
        self.selectPlayerSide()

        # GUI ITEMS
        # Player Side Select Radio Buttons
        self.Ui.radioButton_p1.clicked.connect(self.selectPlayerSide)
        self.Ui.radioButton_p2.clicked.connect(self.selectPlayerSide)
        # PunishBot On Off
        self.Ui.checkBox_punishBot.stateChanged.connect(self.updateBotOptions)
        # Stay On The Ground On Off
        self.Ui.checkBox_stayOnTheGround.stateChanged.connect(
            self.updateBotOptions)
        # Escape From Throws On Off
        self.Ui.checkBox_escapeFromThrows.stateChanged.connect(
            self.updateBotOptions)
        # Defend Type Select Radio Buttons
        self.Ui.radioButton_blockAll.clicked.connect(self.updateBotOptions)
        self.Ui.radioButton_blockHigh.clicked.connect(self.updateBotOptions)
        self.Ui.radioButton_blockLow.clicked.connect(self.updateBotOptions)
        # Low Attack Defend Type Select Radio Buttons
        self.Ui.radioButton_blockLowAll.clicked.connect(self.updateBotOptions)
        self.Ui.radioButton_parryLow.clicked.connect(self.updateBotOptions)
        self.Ui.radioButton_randomLow.clicked.connect(self.updateBotOptions)

        self.update()
        # update program every 7 milisecond
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_launcher)
        self.timer.start(7)

    # Player Side Select Function
    def selectPlayerSide(self):
        if self.Ui.radioButton_p1.isChecked():
            self.selectedPlayer = True
        elif self.Ui.radioButton_p2.isChecked():
            self.selectedPlayer = False
        print(self.selectedPlayer)
        self.update()

    # PunishBot On Off Function
    def updateBotOptions(self):
        self.isPunishmentOn = self.Ui.checkBox_punishBot.isChecked()
        self.stayOnTheGround = self.Ui.checkBox_stayOnTheGround.isChecked()
        self.escapeFromThrows = self.Ui.checkBox_escapeFromThrows.isChecked()
        if self.Ui.radioButton_blockAll.isChecked():
            self.blockType = self.Ui.radioButton_blockAll.text()
        elif self.Ui.radioButton_blockHigh.isChecked():
            self.blockType = self.Ui.radioButton_blockHigh.text()
        elif self.Ui.radioButton_blockLow.isChecked():
            self.blockType = self.Ui.radioButton_blockLow.text()
        self.botOptions = BotOptions(
            isPunishmentOn=self.isPunishmentOn, stayOnTheGround=self.stayOnTheGround, escapeFromThrows=self.escapeFromThrows, blockType=self.blockType)
        self.update()

    def update_launcher(self):
        self.launcher.Update()

    def update(self):
        self.launcher = TekkenBotLauncher(
            BotFrameTrap, self.selectedPlayer, botOptions=self.botOptions)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
