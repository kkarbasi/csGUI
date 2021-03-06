# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1015)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 1015))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 1015))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(100, 30, 89, 25))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.label_filename = QtWidgets.QLabel(self.centralwidget)
        self.label_filename.setGeometry(QtCore.QRect(250, 20, 711, 41))
        self.label_filename.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_filename.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_filename.setText("")
        self.label_filename.setObjectName("label_filename")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 1301, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plotWidget = MplWidget(self.tab)
        self.plotWidget.setGeometry(QtCore.QRect(0, 10, 1291, 371))
        self.plotWidget.setObjectName("plotWidget")
        self.plotWidget_2 = MplWidget(self.tab)
        self.plotWidget_2.setGeometry(QtCore.QRect(0, 400, 1291, 371))
        self.plotWidget_2.setObjectName("plotWidget_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(False)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_isCS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_isCS.setGeometry(QtCore.QRect(1360, 170, 221, 291))
        self.pushButton_isCS.setObjectName("pushButton_isCS")
        self.pushButton_notCS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_notCS.setGeometry(QtCore.QRect(1360, 510, 221, 291))
        self.pushButton_notCS.setObjectName("pushButton_notCS")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(730, 930, 221, 41))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setGeometry(QtCore.QRect(480, 930, 221, 41))
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1350, 860, 81, 17))
        self.label.setObjectName("label")
        self.label_spikeindex = QtWidgets.QLabel(self.centralwidget)
        self.label_spikeindex.setGeometry(QtCore.QRect(1440, 850, 151, 31))
        self.label_spikeindex.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_spikeindex.setText("")
        self.label_spikeindex.setObjectName("label_spikeindex")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 890, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_isCS = QtWidgets.QLabel(self.centralwidget)
        self.label_isCS.setGeometry(QtCore.QRect(640, 891, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_isCS.setFont(font)
        self.label_isCS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_isCS.setText("")
        self.label_isCS.setObjectName("label_isCS")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1410, 889, 41, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_goto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_goto.setGeometry(QtCore.QRect(1460, 890, 111, 31))
        self.lineEdit_goto.setObjectName("lineEdit_goto")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1350, 820, 81, 17))
        self.label_4.setObjectName("label_4")
        self.label_spiketime = QtWidgets.QLabel(self.centralwidget)
        self.label_spiketime.setGeometry(QtCore.QRect(1440, 810, 151, 31))
        self.label_spiketime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_spiketime.setText("")
        self.label_spiketime.setObjectName("label_spiketime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Is this a Complex Spike?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Options"))
        self.pushButton_isCS.setText(_translate("MainWindow", "YES (Q)"))
        self.pushButton_notCS.setText(_translate("MainWindow", "NO (S)"))
        self.pushButton_next.setText(_translate("MainWindow", ">>> (\')"))
        self.pushButton_previous.setText(_translate("MainWindow", "(L) <<<"))
        self.label.setText(_translate("MainWindow", "Spike index:"))
        self.label_2.setText(_translate("MainWindow", "Is CS?"))
        self.label_3.setText(_translate("MainWindow", "Go to"))
        self.label_4.setText(_translate("MainWindow", "Spike time:"))

from mplwidget import MplWidget
