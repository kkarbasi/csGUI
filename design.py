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
        MainWindow.resize(1103, 1015)
        MainWindow.setMinimumSize(QtCore.QSize(1103, 1015))
        MainWindow.setMaximumSize(QtCore.QSize(1103, 1015))
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
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 791, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plotWidget = MplWidget(self.tab)
        self.plotWidget.setGeometry(QtCore.QRect(0, 10, 781, 371))
        self.plotWidget.setObjectName("plotWidget")
        self.plotWidget_2 = MplWidget(self.tab)
        self.plotWidget_2.setGeometry(QtCore.QRect(0, 400, 781, 371))
        self.plotWidget_2.setObjectName("plotWidget_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_isCS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_isCS.setGeometry(QtCore.QRect(850, 190, 221, 291))
        self.pushButton_isCS.setObjectName("pushButton_isCS")
        self.pushButton_notCS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_notCS.setGeometry(QtCore.QRect(850, 490, 221, 311))
        self.pushButton_notCS.setObjectName("pushButton_notCS")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(460, 910, 221, 41))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setGeometry(QtCore.QRect(210, 910, 221, 41))
        self.pushButton_previous.setObjectName("pushButton_previous")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 22))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Is It Complex Spike?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Options"))
        self.pushButton_isCS.setText(_translate("MainWindow", "YES"))
        self.pushButton_notCS.setText(_translate("MainWindow", "NO"))
        self.pushButton_next.setText(_translate("MainWindow", ">>>"))
        self.pushButton_previous.setText(_translate("MainWindow", "<<<"))

from mplwidget import MplWidget
