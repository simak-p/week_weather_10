# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'favorites_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QHBoxLayout, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog_favorites(object):
    def setupUi(self, Dialog_favorites):
        if not Dialog_favorites.objectName():
            Dialog_favorites.setObjectName(u"Dialog_favorites")
        Dialog_favorites.resize(600, 400)
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        Dialog_favorites.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(Dialog_favorites)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QListView(Dialog_favorites)
        self.listView.setObjectName(u"listView")
        self.listView.setEditTriggers(QAbstractItemView.EditKeyPressed)
        self.listView.setAlternatingRowColors(True)
        self.listView.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.listView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_abc = QPushButton(Dialog_favorites)
        self.pushButton_abc.setObjectName(u"pushButton_abc")

        self.horizontalLayout.addWidget(self.pushButton_abc)

        self.pushButton_popularity = QPushButton(Dialog_favorites)
        self.pushButton_popularity.setObjectName(u"pushButton_popularity")

        self.horizontalLayout.addWidget(self.pushButton_popularity)

        self.pushButton_delete = QPushButton(Dialog_favorites)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout.addWidget(self.pushButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog_favorites)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_favorites)

        QMetaObject.connectSlotsByName(Dialog_favorites)
    # setupUi

    def retranslateUi(self, Dialog_favorites):
        Dialog_favorites.setWindowTitle(QCoreApplication.translate("Dialog_favorites", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.pushButton_abc.setText(QCoreApplication.translate("Dialog_favorites", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\n"
"\u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0443", None))
        self.pushButton_popularity.setText(QCoreApplication.translate("Dialog_favorites", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\n"
"\u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u0438", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Dialog_favorites", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437\n"
"\u0438\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e", None))
    # retranslateUi

