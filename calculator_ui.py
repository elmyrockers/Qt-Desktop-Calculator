# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(265, 439)
        MainWindow.setMinimumSize(QSize(265, 439))
        MainWindow.setMaximumSize(QSize(265, 439))
        icon = QIcon()
        icon.addFile(u"calculator-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        font = QFont()
        self.menuExit.setFont(font)
        self.menuCopy = QAction(MainWindow)
        self.menuCopy.setObjectName(u"menuCopy")
        self.menuPaste = QAction(MainWindow)
        self.menuPaste.setObjectName(u"menuPaste")
        self.menuStandard = QAction(MainWindow)
        self.menuStandard.setObjectName(u"menuStandard")
        self.menuScientificMode = QAction(MainWindow)
        self.menuScientificMode.setObjectName(u"menuScientificMode")
        self.menuAboutApp = QAction(MainWindow)
        self.menuAboutApp.setObjectName(u"menuAboutApp")
        self.menuAboutDeveloper = QAction(MainWindow)
        self.menuAboutDeveloper.setObjectName(u"menuAboutDeveloper")
        self.menuVisitWebsite = QAction(MainWindow)
        self.menuVisitWebsite.setObjectName(u"menuVisitWebsite")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(265, 396))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 60))
        self.lineEdit.setMaximumSize(QSize(245, 60))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"padding:10px")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb7 = QPushButton(self.centralwidget)
        self.pb7.setObjectName(u"pb7")
        self.pb7.setMinimumSize(QSize(60, 60))
        self.pb7.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Helvetica"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.pb7.setFont(font2)

        self.gridLayout.addWidget(self.pb7, 1, 0, 1, 1)

        self.pb4 = QPushButton(self.centralwidget)
        self.pb4.setObjectName(u"pb4")
        self.pb4.setMinimumSize(QSize(60, 60))
        self.pb4.setMaximumSize(QSize(60, 60))
        self.pb4.setFont(font2)

        self.gridLayout.addWidget(self.pb4, 4, 0, 1, 1)

        self.pbAdd = QPushButton(self.centralwidget)
        self.pbAdd.setObjectName(u"pbAdd")
        self.pbAdd.setMinimumSize(QSize(60, 60))
        self.pbAdd.setMaximumSize(QSize(60, 60))
        self.pbAdd.setFont(font2)

        self.gridLayout.addWidget(self.pbAdd, 6, 3, 1, 1)

        self.pb6 = QPushButton(self.centralwidget)
        self.pb6.setObjectName(u"pb6")
        self.pb6.setMinimumSize(QSize(60, 60))
        self.pb6.setMaximumSize(QSize(60, 60))
        self.pb6.setFont(font2)

        self.gridLayout.addWidget(self.pb6, 4, 2, 1, 1)

        self.pbDot = QPushButton(self.centralwidget)
        self.pbDot.setObjectName(u"pbDot")
        self.pbDot.setMinimumSize(QSize(60, 60))
        self.pbDot.setMaximumSize(QSize(60, 60))
        self.pbDot.setFont(font2)

        self.gridLayout.addWidget(self.pbDot, 6, 1, 1, 1)

        self.pb0 = QPushButton(self.centralwidget)
        self.pb0.setObjectName(u"pb0")
        self.pb0.setMinimumSize(QSize(60, 60))
        self.pb0.setMaximumSize(QSize(60, 60))
        self.pb0.setFont(font2)

        self.gridLayout.addWidget(self.pb0, 6, 0, 1, 1)

        self.pb5 = QPushButton(self.centralwidget)
        self.pb5.setObjectName(u"pb5")
        self.pb5.setMinimumSize(QSize(60, 60))
        self.pb5.setMaximumSize(QSize(60, 60))
        self.pb5.setFont(font2)

        self.gridLayout.addWidget(self.pb5, 4, 1, 1, 1)

        self.pb8 = QPushButton(self.centralwidget)
        self.pb8.setObjectName(u"pb8")
        self.pb8.setMinimumSize(QSize(60, 60))
        self.pb8.setMaximumSize(QSize(60, 60))
        self.pb8.setFont(font2)

        self.gridLayout.addWidget(self.pb8, 1, 1, 1, 1)

        self.pb3 = QPushButton(self.centralwidget)
        self.pb3.setObjectName(u"pb3")
        self.pb3.setMinimumSize(QSize(60, 60))
        self.pb3.setMaximumSize(QSize(60, 60))
        self.pb3.setFont(font2)

        self.gridLayout.addWidget(self.pb3, 5, 2, 1, 1)

        self.pbEqual = QPushButton(self.centralwidget)
        self.pbEqual.setObjectName(u"pbEqual")
        self.pbEqual.setMinimumSize(QSize(60, 60))
        self.pbEqual.setMaximumSize(QSize(60, 60))
        self.pbEqual.setFont(font2)

        self.gridLayout.addWidget(self.pbEqual, 6, 2, 1, 1)

        self.pbC = QPushButton(self.centralwidget)
        self.pbC.setObjectName(u"pbC")
        self.pbC.setMinimumSize(QSize(60, 60))
        self.pbC.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamilies([u"Helvetica"])
        font3.setPointSize(14)
        self.pbC.setFont(font3)

        self.gridLayout.addWidget(self.pbC, 0, 0, 1, 1)

        self.pb9 = QPushButton(self.centralwidget)
        self.pb9.setObjectName(u"pb9")
        self.pb9.setMinimumSize(QSize(60, 60))
        self.pb9.setMaximumSize(QSize(60, 60))
        self.pb9.setFont(font2)

        self.gridLayout.addWidget(self.pb9, 1, 2, 1, 1)

        self.pb2 = QPushButton(self.centralwidget)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setMinimumSize(QSize(60, 60))
        self.pb2.setMaximumSize(QSize(60, 60))
        self.pb2.setFont(font2)

        self.gridLayout.addWidget(self.pb2, 5, 1, 1, 1)

        self.pbDivide = QPushButton(self.centralwidget)
        self.pbDivide.setObjectName(u"pbDivide")
        self.pbDivide.setMinimumSize(QSize(60, 60))
        self.pbDivide.setMaximumSize(QSize(60, 60))
        self.pbDivide.setFont(font2)

        self.gridLayout.addWidget(self.pbDivide, 1, 3, 1, 1)

        self.pbMultiply = QPushButton(self.centralwidget)
        self.pbMultiply.setObjectName(u"pbMultiply")
        self.pbMultiply.setMinimumSize(QSize(60, 60))
        self.pbMultiply.setMaximumSize(QSize(60, 60))
        self.pbMultiply.setFont(font2)

        self.gridLayout.addWidget(self.pbMultiply, 4, 3, 1, 1)

        self.pb1 = QPushButton(self.centralwidget)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setMinimumSize(QSize(60, 60))
        self.pb1.setMaximumSize(QSize(60, 60))
        self.pb1.setFont(font2)

        self.gridLayout.addWidget(self.pb1, 5, 0, 1, 1)

        self.pbSubtract = QPushButton(self.centralwidget)
        self.pbSubtract.setObjectName(u"pbSubtract")
        self.pbSubtract.setMinimumSize(QSize(60, 60))
        self.pbSubtract.setMaximumSize(QSize(60, 60))
        self.pbSubtract.setFont(font2)

        self.gridLayout.addWidget(self.pbSubtract, 5, 3, 1, 1)

        self.pbBackspace = QPushButton(self.centralwidget)
        self.pbBackspace.setObjectName(u"pbBackspace")
        self.pbBackspace.setMinimumSize(QSize(60, 60))
        self.pbBackspace.setMaximumSize(QSize(60, 60))
        self.pbBackspace.setFont(font3)

        self.gridLayout.addWidget(self.pbBackspace, 0, 1, 1, 1)

        self.pbPercent = QPushButton(self.centralwidget)
        self.pbPercent.setObjectName(u"pbPercent")
        self.pbPercent.setMinimumSize(QSize(60, 60))
        self.pbPercent.setMaximumSize(QSize(60, 60))
        self.pbPercent.setFont(font3)

        self.gridLayout.addWidget(self.pbPercent, 0, 2, 1, 1)

        self.pbCE = QPushButton(self.centralwidget)
        self.pbCE.setObjectName(u"pbCE")
        self.pbCE.setMinimumSize(QSize(60, 60))
        self.pbCE.setMaximumSize(QSize(60, 60))
        self.pbCE.setFont(font3)

        self.gridLayout.addWidget(self.pbCE, 0, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 265, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuExit)
        self.menuEdit.addAction(self.menuCopy)
        self.menuEdit.addAction(self.menuPaste)
        self.menuView.addAction(self.menuStandard)
        self.menuView.addAction(self.menuScientificMode)
        self.menuHelp.addAction(self.menuAboutApp)
        self.menuHelp.addAction(self.menuAboutDeveloper)
        self.menuHelp.addAction(self.menuVisitWebsite)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qt Desktop Calculator (by elmyrockers)", None))
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.menuPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.menuStandard.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.menuScientificMode.setText(QCoreApplication.translate("MainWindow", u"Scientific Mode", None))
        self.menuAboutApp.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.menuAboutDeveloper.setText(QCoreApplication.translate("MainWindow", u"About Developer", None))
        self.menuVisitWebsite.setText(QCoreApplication.translate("MainWindow", u"Visit Website", None))
        self.pb7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pb4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pbAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pb6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pbDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pb0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pb5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pb8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pb3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pbEqual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pbC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pb9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pb2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pbDivide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pbMultiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pb1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pbSubtract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pbBackspace.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pbPercent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pbCE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

