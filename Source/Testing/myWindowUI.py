# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 475)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 531, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 231, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.titleVerticleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.titleVerticleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleVerticleLayout.setObjectName("titleVerticleLayout")
        self.youtubeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.youtubeLabel.setFont(font)
        self.youtubeLabel.setObjectName("youtubeLabel")
        self.titleVerticleLayout.addWidget(self.youtubeLabel)
        self.qrcodescraperLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        
        self.qrcodescraperLabel.setFont(font)
        self.qrcodescraperLabel.setObjectName("qrcodescraperLabel")
        self.titleVerticleLayout.addWidget(self.qrcodescraperLabel)
        self.creatorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.creatorLabel.setObjectName("creatorLabel")
        self.titleVerticleLayout.addWidget(self.creatorLabel)
        self.displayVideosCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.displayVideosCheckBox.setObjectName("displayVideosCheckBox")
        self.titleVerticleLayout.addWidget(self.displayVideosCheckBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(19, 293, 481, 94))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.outputVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.outputVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.outputVerticalLayout.setObjectName("outputVerticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.outputLabel.setObjectName("outputLabel")
        self.outputVerticalLayout.addWidget(self.outputLabel)
        self.outputListView = QtWidgets.QListView(self.verticalLayoutWidget_3)
        self.outputListView.setObjectName("outputListView")
        self.outputVerticalLayout.addWidget(self.outputListView)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 231, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.urlVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.urlVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.urlVerticalLayout.setObjectName("urlVerticalLayout")
        self.youtubeUrlLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.youtubeUrlLabel.setObjectName("youtubeUrlLabel")
        self.urlVerticalLayout.addWidget(self.youtubeUrlLabel)
        self.userLinkEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.userLinkEdit.setObjectName("userLinkEdit")
        self.urlVerticalLayout.addWidget(self.userLinkEdit)
        self.getWebsitesCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.getWebsitesCheckBox.setObjectName("getWebsitesCheckBox")
        self.urlVerticalLayout.addWidget(self.getWebsitesCheckBox)
        self.getTcgCodesCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.getTcgCodesCheckBox.setObjectName("getTcgCodesCheckBox")
        self.urlVerticalLayout.addWidget(self.getTcgCodesCheckBox)
        self.searchLinkCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.searchLinkCheckBox.setObjectName("searchLinkCheckBox")
        self.urlVerticalLayout.addWidget(self.searchLinkCheckBox)
        self.addVideoButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addVideoButton.setObjectName("addVideoButton")
        self.urlVerticalLayout.addWidget(self.addVideoButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 20, 231, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.queueVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.queueVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.queueVerticalLayout.setObjectName("queueVerticalLayout")
        self.videoQueueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.videoQueueLabel.setObjectName("videoQueueLabel")
        self.queueVerticalLayout.addWidget(self.videoQueueLabel)
        self.videoQueueListView = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.videoQueueListView.setObjectName("videoQueueListView")
        self.queueVerticalLayout.addWidget(self.videoQueueListView)
        self.scanVideosButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.scanVideosButton.setObjectName("scanVideosButton")
        self.queueVerticalLayout.addWidget(self.scanVideosButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 411, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.aboutVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.aboutVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutVerticalLayout.setObjectName("aboutVerticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.aboutVerticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.aboutVerticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.aboutVerticalLayout.addWidget(self.label_8)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.youtubeLabel.setText(_translate("MainWindow", "Youtube"))
        self.qrcodescraperLabel.setText(_translate("MainWindow", "QR Code Scraper"))
        self.creatorLabel.setText(_translate("MainWindow", "by Tom Opolski"))
        self.displayVideosCheckBox.setText(_translate("MainWindow", "Display videos being processed"))
        self.outputLabel.setText(_translate("MainWindow", "Output List"))
        self.youtubeUrlLabel.setText(_translate("MainWindow", "YouTube URL:"))
        self.userLinkEdit.setText(_translate("MainWindow", "https://www.youtube.com/watch?v=oAcumtLhp58"))
        self.getWebsitesCheckBox.setText(_translate("MainWindow", "Get Websites"))
        self.getTcgCodesCheckBox.setText(_translate("MainWindow", "Get PKMN TCG Codes"))
        self.searchLinkCheckBox.setText(_translate("MainWindow", "Search link (vs. Video Link)"))
        self.addVideoButton.setText(_translate("MainWindow", "Add to Video Queue"))
        self.videoQueueLabel.setText(_translate("MainWindow", "Video Queue"))
        self.scanVideosButton.setText(_translate("MainWindow", "Scan Videos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "QR Scraper"))
        self.label_6.setText(_translate("MainWindow", "Created by: Thomas Opolski"))
        self.label_7.setText(_translate("MainWindow", "Date: 12/30/19"))
        self.label_8.setText(_translate("MainWindow", "Website: https://github.com/opolskitom (I really need a website)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About"))
