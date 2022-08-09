# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(672, 384)
        self.action_chart_week = QAction(MainWindow)
        self.action_chart_week.setObjectName(u"action_chart_week")
        self.action_chart_three = QAction(MainWindow)
        self.action_chart_three.setObjectName(u"action_chart_three")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_city = QLabel(self.centralwidget)
        self.label_city.setObjectName(u"label_city")
        self.label_city.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_city)

        self.lineEdit_Cyty = QLineEdit(self.centralwidget)
        self.lineEdit_Cyty.setObjectName(u"lineEdit_Cyty")

        self.horizontalLayout.addWidget(self.lineEdit_Cyty)

        self.pushButtonsearce = QPushButton(self.centralwidget)
        self.pushButtonsearce.setObjectName(u"pushButtonsearce")

        self.horizontalLayout.addWidget(self.pushButtonsearce)

        self.pushButton_favorites = QPushButton(self.centralwidget)
        self.pushButton_favorites.setObjectName(u"pushButton_favorites")

        self.horizontalLayout.addWidget(self.pushButton_favorites)

        self.pushButton_history = QPushButton(self.centralwidget)
        self.pushButton_history.setObjectName(u"pushButton_history")

        self.horizontalLayout.addWidget(self.pushButton_history)

        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 632, 267))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_0 = QLabel(self.scrollAreaWidgetContents)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setFrameShape(QFrame.Box)
        self.label_0.setFrameShadow(QFrame.Raised)
        self.label_0.setLineWidth(2)
        self.label_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_0)

        self.label_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFrameShape(QFrame.Box)
        self.label_1.setFrameShadow(QFrame.Raised)
        self.label_1.setLineWidth(2)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Raised)
        self.label_4.setLineWidth(2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setLineWidth(2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_6.setLineWidth(2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setFrameShadow(QFrame.Raised)
        self.label_7.setLineWidth(2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 672, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_chart_week)
        self.menu.addAction(self.action_chart_three)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_chart_week.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.action_chart_three.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u0442\u0440\u0438 \u0434\u043d\u044f", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", u"\u0433\u043e\u0440\u043e\u0434:", None))
        self.pushButtonsearce.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_favorites.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.pushButton_history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e\u0433\u043e\u0434\u044b", None))
    # retranslateUi

