# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_charts.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog_charts(object):
    def setupUi(self, Dialog_charts):
        if not Dialog_charts.objectName():
            Dialog_charts.setObjectName(u"Dialog_charts")
        Dialog_charts.resize(757, 400)
        Dialog_charts.setStyleSheet(u"font: italic 12pt \"Sans Serif\";")
        self.verticalLayout_2 = QVBoxLayout(Dialog_charts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(Dialog_charts)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSlider = QSlider(Dialog_charts)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Dialog_charts)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_week = QComboBox(Dialog_charts)
        self.comboBox_week.setObjectName(u"comboBox_week")

        self.horizontalLayout.addWidget(self.comboBox_week)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_charts)

        QMetaObject.connectSlotsByName(Dialog_charts)
    # setupUi

    def retranslateUi(self, Dialog_charts):
        Dialog_charts.setWindowTitle(QCoreApplication.translate("Dialog_charts", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e\u0433\u043e\u0434\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_charts", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431: ", None))
        self.label.setText(QCoreApplication.translate("Dialog_charts", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 : ", None))
    # retranslateUi

