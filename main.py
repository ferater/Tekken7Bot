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
        # Check if PunishBot is on or off
        self.punishBotOnOff()
        # Check player side on bot start
        self.selectPlayerSide()
        # # set BotOptions
        # self.botOptions = BotOptions(
        #     isPunishmentOn=self.isPunishmentOn, stayOnTheGround=self.stayOnTheGround)
        # Player Side Select Radio Buttons
        self.Ui.radioButton_p1.clicked.connect(self.selectPlayerSide)
        self.Ui.radioButton_p2.clicked.connect(self.selectPlayerSide)
        # PunishBot On Off Radio Buttons
        self.Ui.radioButton_punishBot_on.clicked.connect(self.punishBotOnOff)
        self.Ui.radioButton_punishBot_off.clicked.connect(self.punishBotOnOff)
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
        # set BotOptions
        self.update()

    # PunishBot On Off Function

    def punishBotOnOff(self):
        if self.Ui.radioButton_punishBot_on.isChecked():
            self.isPunishmentOn = True
            self.Ui.label_punish.setText("Punish is on")
        else:
            self.isPunishmentOn = False
            self.Ui.label_punish.setText("Punish is off")
        self.botOptions = BotOptions(
            isPunishmentOn=self.isPunishmentOn, stayOnTheGround=self.stayOnTheGround)
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
