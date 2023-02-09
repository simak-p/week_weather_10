# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searce_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_searce(object):
    def setupUi(self, Dialog_searce):
        if not Dialog_searce.objectName():
            Dialog_searce.setObjectName(u"Dialog_searce")
        Dialog_searce.resize(593, 300)
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        Dialog_searce.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog_searce)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog_searce)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_searce = QLineEdit(Dialog_searce)
        self.lineEdit_searce.setObjectName(u"lineEdit_searce")
        self.lineEdit_searce.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_searce)

        self.pushButton_searce = QPushButton(Dialog_searce)
        self.pushButton_searce.setObjectName(u"pushButton_searce")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_searce.sizePolicy().hasHeightForWidth())
        self.pushButton_searce.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_searce)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView_searce = QListView(Dialog_searce)
        self.listView_searce.setObjectName(u"listView_searce")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView_searce.sizePolicy().hasHeightForWidth())
        self.listView_searce.setSizePolicy(sizePolicy1)
        self.listView_searce.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listView_searce.setAlternatingRowColors(True)
        self.listView_searce.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.listView_searce)

        self.buttonBox = QDialogButtonBox(Dialog_searce)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_searce)
        self.buttonBox.rejected.connect(Dialog_searce.reject)
        self.buttonBox.accepted.connect(Dialog_searce.accept)

        QMetaObject.connectSlotsByName(Dialog_searce)
    # setupUi

    def retranslateUi(self, Dialog_searce):
        Dialog_searce.setWindowTitle(QCoreApplication.translate("Dialog_searce", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0433\u043e\u0440\u043e\u0434\u0430\u043c", None))
        self.label.setText(QCoreApplication.translate("Dialog_searce", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430:  ", None))
        self.lineEdit_searce.setText("")
        self.lineEdit_searce.setPlaceholderText("")
        self.pushButton_searce.setText(QCoreApplication.translate("Dialog_searce", u"\u0418\u0441\u043a\u0430\u0442\u044c", None))
    # retranslateUi

