# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_searce.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QListView, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 430)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listView.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.SelectedClicked)
        self.listView.setTabKeyNavigation(True)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listView.setMovement(QListView.Snap)
        self.listView.setFlow(QListView.TopToBottom)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setViewMode(QListView.ListMode)
        self.listView.setModelColumn(0)
        self.listView.setItemAlignment(Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.listView)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

