# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Aug 23 16:13:29 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName(_fromUtf8("settings"))
        settings.resize(400, 310)
        self.gridLayout_2 = QtGui.QGridLayout(settings)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.settingsTab = QtGui.QTabWidget(settings)
        self.settingsTab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 60, 220, 26))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.fetchFreqSpin = QtGui.QSpinBox(self.layoutWidget)
        self.fetchFreqSpin.setMinimum(1)
        self.fetchFreqSpin.setMaximum(1440)
        self.fetchFreqSpin.setProperty(_fromUtf8("value"), 60)
        self.fetchFreqSpin.setObjectName(_fromUtf8("fetchFreqSpin"))
        self.horizontalLayout_2.addWidget(self.fetchFreqSpin)
        self.settingsTab.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.popUpChk = QtGui.QCheckBox(self.tab_3)
        self.popUpChk.setGeometry(QtCore.QRect(80, 56, 181, 22))
        self.popUpChk.setObjectName(_fromUtf8("popUpChk"))
        self.SysBellChk = QtGui.QCheckBox(self.tab_3)
        self.SysBellChk.setGeometry(QtCore.QRect(80, 100, 181, 22))
        self.SysBellChk.setObjectName(_fromUtf8("SysBellChk"))
        self.disableAllChk = QtGui.QCheckBox(self.tab_3)
        self.disableAllChk.setGeometry(QtCore.QRect(81, 140, 201, 22))
        self.disableAllChk.setObjectName(_fromUtf8("disableAllChk"))
        self.settingsTab.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.speedSpin = QtGui.QSpinBox(self.tab_2)
        self.speedSpin.setMinimum(80)
        self.speedSpin.setMaximum(440)
        self.speedSpin.setProperty(_fromUtf8("value"), 150)
        self.speedSpin.setObjectName(_fromUtf8("speedSpin"))
        self.horizontalLayout_5.addWidget(self.speedSpin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.pitchSpin = QtGui.QSpinBox(self.tab_2)
        self.pitchSpin.setMinimum(0)
        self.pitchSpin.setMaximum(99)
        self.pitchSpin.setProperty(_fromUtf8("value"), 40)
        self.pitchSpin.setObjectName(_fromUtf8("pitchSpin"))
        self.horizontalLayout_4.addWidget(self.pitchSpin)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        self.settingsTab.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.twitterRemLoginChk = QtGui.QCheckBox(self.tab_4)
        self.twitterRemLoginChk.setGeometry(QtCore.QRect(80, 40, 151, 22))
        self.twitterRemLoginChk.setObjectName(_fromUtf8("twitterRemLoginChk"))
        self.settingsTab.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.rilRemLoginChk = QtGui.QCheckBox(self.tab_5)
        self.rilRemLoginChk.setGeometry(QtCore.QRect(80, 40, 151, 22))
        self.rilRemLoginChk.setObjectName(_fromUtf8("rilRemLoginChk"))
        self.settingsTab.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.settingsTab, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem7 = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.btnSave = QtGui.QPushButton(settings)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave)
        spacerItem8 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.btnCancel = QtGui.QPushButton(settings)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(settings)
        self.settingsTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "feedIO Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("settings", "Feed fetching frequncy (Minutes)", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab), QtGui.QApplication.translate("settings", " General", None, QtGui.QApplication.UnicodeUTF8))
        self.popUpChk.setText(QtGui.QApplication.translate("settings", "Pop up Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.SysBellChk.setText(QtGui.QApplication.translate("settings", "System bells updates", None, QtGui.QApplication.UnicodeUTF8))
        self.disableAllChk.setText(QtGui.QApplication.translate("settings", "Disable All Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab_3), QtGui.QApplication.translate("settings", "Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settings", "Text to speech Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settings", "Text to speech Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab_2), QtGui.QApplication.translate("settings", "Text to speech", None, QtGui.QApplication.UnicodeUTF8))
        self.twitterRemLoginChk.setText(QtGui.QApplication.translate("settings", "&Remember Login Session", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab_4), QtGui.QApplication.translate("settings", "Twitter", None, QtGui.QApplication.UnicodeUTF8))
        self.rilRemLoginChk.setText(QtGui.QApplication.translate("settings", "&Remember Login Session", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab_5), QtGui.QApplication.translate("settings", "Read It Later", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("settings", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("settings", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

