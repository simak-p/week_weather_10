# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 442)
        self.action_searce = QAction(MainWindow)
        self.action_searce.setObjectName(u"action_searce")
        self.action_searce.setCheckable(True)
        self.action_favorites = QAction(MainWindow)
        self.action_favorites.setObjectName(u"action_favorites")
        self.action_favorites.setCheckable(True)
        self.action_history = QAction(MainWindow)
        self.action_history.setObjectName(u"action_history")
        self.action_history.setCheckable(True)
        self.action_charts = QAction(MainWindow)
        self.action_charts.setObjectName(u"action_charts")
        self.action_searce_show = QAction(MainWindow)
        self.action_searce_show.setObjectName(u"action_searce_show")
        self.action_searce_close = QAction(MainWindow)
        self.action_searce_close.setObjectName(u"action_searce_close")
        self.action_favorites_show = QAction(MainWindow)
        self.action_favorites_show.setObjectName(u"action_favorites_show")
        self.action_favorites_close = QAction(MainWindow)
        self.action_favorites_close.setObjectName(u"action_favorites_close")
        self.action_history_show = QAction(MainWindow)
        self.action_history_show.setObjectName(u"action_history_show")
        self.action_history_close = QAction(MainWindow)
        self.action_history_close.setObjectName(u"action_history_close")
        self.action_sharts_show = QAction(MainWindow)
        self.action_sharts_show.setObjectName(u"action_sharts_show")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 134, 386))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_0 = QLabel(self.scrollAreaWidgetContents)
        self.icon_0.setObjectName(u"icon_0")
        self.icon_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_0, 1, 0, 1, 1)

        self.icon_1 = QLabel(self.scrollAreaWidgetContents)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_1, 2, 0, 1, 1)

        self.icon_2 = QLabel(self.scrollAreaWidgetContents)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_2, 3, 0, 1, 1)

        self.icon_3 = QLabel(self.scrollAreaWidgetContents)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_3, 4, 0, 1, 1)

        self.icon_4 = QLabel(self.scrollAreaWidgetContents)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_4, 5, 0, 1, 1)

        self.icon_5 = QLabel(self.scrollAreaWidgetContents)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_5, 6, 0, 1, 1)

        self.icon_6 = QLabel(self.scrollAreaWidgetContents)
        self.icon_6.setObjectName(u"icon_6")
        self.icon_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_6, 7, 0, 1, 1)

        self.icon = QLabel(self.scrollAreaWidgetContents)
        self.icon.setObjectName(u"icon")
        self.icon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_0 = QLabel(self.scrollAreaWidgetContents)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_0, 1, 1, 1, 1)

        self.label_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 2, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_searce = QDockWidget(MainWindow)
        self.dockWidget_searce.setObjectName(u"dockWidget_searce")
        self.dockWidget_searce.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_searce.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_7 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_19 = QLabel(self.dockWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_3.addWidget(self.label_19)

        self.lineEdit_searce = QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_searce.setObjectName(u"lineEdit_searce")

        self.horizontalLayout_3.addWidget(self.lineEdit_searce)

        self.pushButton_searce = QPushButton(self.dockWidgetContents_2)
        self.pushButton_searce.setObjectName(u"pushButton_searce")

        self.horizontalLayout_3.addWidget(self.pushButton_searce)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.listView_searce = QListView(self.dockWidgetContents_2)
        self.listView_searce.setObjectName(u"listView_searce")
        self.listView_searce.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listView_searce.setAlternatingRowColors(True)

        self.verticalLayout_6.addWidget(self.listView_searce)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.dockWidget_searce.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_searce)
        self.dockWidget_history = QDockWidget(MainWindow)
        self.dockWidget_history.setObjectName(u"dockWidget_history")
        self.dockWidget_history.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_history.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView_history = QListView(self.dockWidgetContents)
        self.listView_history.setObjectName(u"listView_history")
        self.listView_history.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listView_history.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.listView_history)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.dockWidget_history.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_history)
        self.dockWidget_favorites = QDockWidget(MainWindow)
        self.dockWidget_favorites.setObjectName(u"dockWidget_favorites")
        self.dockWidget_favorites.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_favorites.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_8 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listView_favorites = QListView(self.dockWidgetContents_3)
        self.listView_favorites.setObjectName(u"listView_favorites")
        self.listView_favorites.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listView_favorites.setAlternatingRowColors(True)

        self.verticalLayout_5.addWidget(self.listView_favorites)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.dockWidget_favorites.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_favorites)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_searce.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.action_favorites.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.action_history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.action_charts.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0430\u0444\u0438\u043a\u0438 \u043f\u043e\u0433\u043e\u0434\u044b", None))
        self.action_searce_show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.action_searce_close.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.action_favorites_show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.action_favorites_close.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.action_history_show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.action_history_close.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.action_sharts_show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.icon_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.dockWidget_searce.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430:", None))
        self.pushButton_searce.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.dockWidget_history.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.dockWidget_favorites.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
    # retranslateUi

