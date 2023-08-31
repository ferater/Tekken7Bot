# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 171, 71))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_p1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_p1.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.radioButton_p1.setObjectName("radioButton_p1")
        self.radioButton_p2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_p2.setGeometry(QtCore.QRect(80, 40, 81, 17))
        self.radioButton_p2.setChecked(True)
        self.radioButton_p2.setObjectName("radioButton_p2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label.setObjectName("label")
        self.groupBox_punishment = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_punishment.setGeometry(QtCore.QRect(10, 90, 171, 51))
        self.groupBox_punishment.setObjectName("groupBox_punishment")
        self.checkBox_punishBot = QtWidgets.QCheckBox(self.groupBox_punishment)
        self.checkBox_punishBot.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.checkBox_punishBot.setObjectName("checkBox_punishBot")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 80, 201, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_stayOnTheGround = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_stayOnTheGround.setGeometry(QtCore.QRect(10, 20, 131, 17))
        self.checkBox_stayOnTheGround.setObjectName("checkBox_stayOnTheGround")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 181, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 171, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_escapeFromThrows = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_escapeFromThrows.setGeometry(QtCore.QRect(10, 20, 141, 17))
        self.checkBox_escapeFromThrows.setObjectName("checkBox_escapeFromThrows")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 151, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 220, 311, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_blockHigh = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_blockHigh.setGeometry(QtCore.QRect(90, 20, 121, 17))
        self.radioButton_blockHigh.setObjectName("radioButton_blockHigh")
        self.radioButton_blockLow = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_blockLow.setGeometry(QtCore.QRect(220, 20, 81, 17))
        self.radioButton_blockLow.setObjectName("radioButton_blockLow")
        self.radioButton_blockAll = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_blockAll.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_blockAll.setObjectName("radioButton_blockAll")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 280, 271, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_parryLow = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_parryLow.setGeometry(QtCore.QRect(70, 20, 61, 17))
        self.radioButton_parryLow.setObjectName("radioButton_parryLow")
        self.radioButton_randomLow = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_randomLow.setGeometry(QtCore.QRect(130, 20, 71, 17))
        self.radioButton_randomLow.setObjectName("radioButton_randomLow")
        self.radioButton_blockLowAll = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_blockLowAll.setGeometry(QtCore.QRect(10, 20, 51, 17))
        self.radioButton_blockLowAll.setObjectName("radioButton_blockLowAll")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tekken7 BotGui"))
        self.groupBox.setTitle(_translate("MainWindow", "Player Select"))
        self.radioButton_p1.setText(_translate("MainWindow", "Player 1"))
        self.radioButton_p2.setText(_translate("MainWindow", "Player 2"))
        self.label.setText(_translate("MainWindow", "Select your side"))
        self.groupBox_punishment.setTitle(_translate("MainWindow", "Punishment"))
        self.checkBox_punishBot.setText(_translate("MainWindow", "Punishment ON"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dont GetUp"))
        self.checkBox_stayOnTheGround.setText(_translate("MainWindow", "Stay On The Ground"))
        self.label_2.setText(_translate("MainWindow", "Useful for some chars like Lei, Eddy.."))
        self.groupBox_2.setTitle(_translate("MainWindow", "ThrowTech"))
        self.checkBox_escapeFromThrows.setText(_translate("MainWindow", "Escape From Throws"))
        self.label_3.setText(_translate("MainWindow", "May not Work on Every Throw"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Defend Attacks"))
        self.radioButton_blockHigh.setText(_translate("MainWindow", "High and Mid Attacks"))
        self.radioButton_blockLow.setText(_translate("MainWindow", "Low Attacks"))
        self.radioButton_blockAll.setText(_translate("MainWindow", "Defend All"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Low Block Style"))
        self.radioButton_parryLow.setText(_translate("MainWindow", "Parry"))
        self.radioButton_randomLow.setText(_translate("MainWindow", "Random"))
        self.radioButton_blockLowAll.setText(_translate("MainWindow", "Block"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
