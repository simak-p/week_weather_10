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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(596, 405)
        self.action_chart_week = QAction(MainWindow)
        self.action_chart_week.setObjectName(u"action_chart_week")
        self.action_favorites = QAction(MainWindow)
        self.action_favorites.setObjectName(u"action_favorites")
        self.action_weather = QAction(MainWindow)
        self.action_weather.setObjectName(u"action_weather")
        self.action_weather_2 = QAction(MainWindow)
        self.action_weather_2.setObjectName(u"action_weather_2")
        self.action_favorites_2 = QAction(MainWindow)
        self.action_favorites_2.setObjectName(u"action_favorites_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_weather = QWidget()
        self.page_weather.setObjectName(u"page_weather")
        self.verticalLayout_3 = QVBoxLayout(self.page_weather)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_city = QLabel(self.page_weather)
        self.label_city.setObjectName(u"label_city")

        self.horizontalLayout.addWidget(self.label_city)

        self.lineEdit_city = QLineEdit(self.page_weather)
        self.lineEdit_city.setObjectName(u"lineEdit_city")

        self.horizontalLayout.addWidget(self.lineEdit_city)

        self.pushButton_searce = QPushButton(self.page_weather)
        self.pushButton_searce.setObjectName(u"pushButton_searce")

        self.horizontalLayout.addWidget(self.pushButton_searce)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.page_weather)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 556, 288))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)

        self.label_0 = QLabel(self.scrollAreaWidgetContents)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_0, 0, 1, 1, 1)

        self.label_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 1, 1, 1, 1)

        self.icon_1 = QLabel(self.scrollAreaWidgetContents)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_1, 0, 0, 1, 1)

        self.icon_2 = QLabel(self.scrollAreaWidgetContents)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_2, 1, 0, 1, 1)

        self.icon_3 = QLabel(self.scrollAreaWidgetContents)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_3, 2, 0, 1, 1)

        self.icon_4 = QLabel(self.scrollAreaWidgetContents)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_4, 3, 0, 1, 1)

        self.icon_5 = QLabel(self.scrollAreaWidgetContents)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_5, 4, 0, 1, 1)

        self.Icon_6 = QLabel(self.scrollAreaWidgetContents)
        self.Icon_6.setObjectName(u"Icon_6")
        self.Icon_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Icon_6, 5, 0, 1, 1)

        self.icon_7 = QLabel(self.scrollAreaWidgetContents)
        self.icon_7.setObjectName(u"icon_7")

        self.gridLayout.addWidget(self.icon_7, 6, 0, 1, 1)

        self.icon_8 = QLabel(self.scrollAreaWidgetContents)
        self.icon_8.setObjectName(u"icon_8")
        self.icon_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_8, 7, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_5.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.page_weather)
        self.page_favorites = QWidget()
        self.page_favorites.setObjectName(u"page_favorites")
        self.horizontalLayout_3 = QHBoxLayout(self.page_favorites)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.page_favorites)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.page_favorites)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listView_favorites = QListView(self.page_favorites)
        self.listView_favorites.setObjectName(u"listView_favorites")

        self.horizontalLayout_4.addWidget(self.listView_favorites)

        self.listView_history = QListView(self.page_favorites)
        self.listView_history.setObjectName(u"listView_history")

        self.horizontalLayout_4.addWidget(self.listView_history)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_favorites)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 596, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_chart_week)
        self.menu.addAction(self.action_weather_2)
        self.menu.addAction(self.action_favorites_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_chart_week.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e\u0433\u043e\u0434\u044b", None))
        self.action_favorites.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.action_weather.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0443", None))
        self.action_weather_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.action_favorites_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430\u0441\u0435\u043b\u0451\u043d\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430:", None))
        self.pushButton_searce.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Icon_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

