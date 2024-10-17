# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))
        self.tbMain = QWidget()
        self.tbMain.setObjectName(u"tbMain")
        self.imgPlot = QLabel(self.tbMain)
        self.imgPlot.setObjectName(u"imgPlot")
        self.imgPlot.setGeometry(QRect(20, 20, 751, 471))
        self.imgPlot.setPixmap(QPixmap(u"plot_placeholder.png"))
        self.btnPlot = QPushButton(self.tbMain)
        self.btnPlot.setObjectName(u"btnPlot")
        self.btnPlot.setGeometry(QRect(350, 500, 83, 29))
        self.tabWidget.addTab(self.tbMain, "")
        self.tbBWB = QWidget()
        self.tbBWB.setObjectName(u"tbBWB")
        self.btnUpdate = QPushButton(self.tbBWB)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(660, 30, 83, 29))
        self.gridLayoutWidget = QWidget(self.tbBWB)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 341, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.txtVertTailSweep = QLineEdit(self.gridLayoutWidget)
        self.txtVertTailSweep.setObjectName(u"txtVertTailSweep")

        self.gridLayout.addWidget(self.txtVertTailSweep, 4, 2, 1, 1)

        self.txtWingSweep = QLineEdit(self.gridLayoutWidget)
        self.txtWingSweep.setObjectName(u"txtWingSweep")

        self.gridLayout.addWidget(self.txtWingSweep, 4, 1, 1, 1)

        self.txtVertTailAspectRatio = QLineEdit(self.gridLayoutWidget)
        self.txtVertTailAspectRatio.setObjectName(u"txtVertTailAspectRatio")

        self.gridLayout.addWidget(self.txtVertTailAspectRatio, 2, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lbTailspan = QLabel(self.gridLayoutWidget)
        self.lbTailspan.setObjectName(u"lbTailspan")

        self.gridLayout.addWidget(self.lbTailspan, 2, 0, 1, 1)

        self.txtWingTaperRatio = QLineEdit(self.gridLayoutWidget)
        self.txtWingTaperRatio.setObjectName(u"txtWingTaperRatio")

        self.gridLayout.addWidget(self.txtWingTaperRatio, 3, 1, 1, 1)

        self.lbWingspan = QLabel(self.gridLayoutWidget)
        self.lbWingspan.setObjectName(u"lbWingspan")

        self.gridLayout.addWidget(self.lbWingspan, 1, 0, 1, 1)

        self.txtVertTailSqFt = QLineEdit(self.gridLayoutWidget)
        self.txtVertTailSqFt.setObjectName(u"txtVertTailSqFt")

        self.gridLayout.addWidget(self.txtVertTailSqFt, 1, 2, 1, 1)

        self.txtWingAspectRatio = QLineEdit(self.gridLayoutWidget)
        self.txtWingAspectRatio.setObjectName(u"txtWingAspectRatio")

        self.gridLayout.addWidget(self.txtWingAspectRatio, 2, 1, 1, 1)

        self.txtVertTailTaperRatio = QLineEdit(self.gridLayoutWidget)
        self.txtVertTailTaperRatio.setObjectName(u"txtVertTailTaperRatio")

        self.gridLayout.addWidget(self.txtVertTailTaperRatio, 3, 2, 1, 1)

        self.txtWingSqFt = QLineEdit(self.gridLayoutWidget)
        self.txtWingSqFt.setObjectName(u"txtWingSqFt")

        self.gridLayout.addWidget(self.txtWingSqFt, 1, 1, 1, 1)

        self.lbWingspan_2 = QLabel(self.gridLayoutWidget)
        self.lbWingspan_2.setObjectName(u"lbWingspan_2")

        self.gridLayout.addWidget(self.lbWingspan_2, 0, 1, 1, 1)

        self.lbWingspan_3 = QLabel(self.gridLayoutWidget)
        self.lbWingspan_3.setObjectName(u"lbWingspan_3")

        self.gridLayout.addWidget(self.lbWingspan_3, 0, 2, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.tbBWB)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 210, 341, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbDropDistance = QLabel(self.gridLayoutWidget_2)
        self.lbDropDistance.setObjectName(u"lbDropDistance")

        self.gridLayout_2.addWidget(self.lbDropDistance, 0, 0, 1, 1)

        self.txtDropDistance = QLineEdit(self.gridLayoutWidget_2)
        self.txtDropDistance.setObjectName(u"txtDropDistance")

        self.gridLayout_2.addWidget(self.txtDropDistance, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tbBWB, "")
        self.tbTW = QWidget()
        self.tbTW.setObjectName(u"tbTW")
        self.tbTW.setEnabled(True)
        self.tabWidget.addTab(self.tbTW, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.imgPlot.setText("")
        self.btnPlot.setText(QCoreApplication.translate("Widget", u"plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbMain), QCoreApplication.translate("Widget", u"Main", None))
        self.btnUpdate.setText(QCoreApplication.translate("Widget", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Sweep:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Taper Ratio:", None))
        self.lbTailspan.setText(QCoreApplication.translate("Widget", u"Aspect Ratio:", None))
        self.lbWingspan.setText(QCoreApplication.translate("Widget", u"Square Footage:", None))
        self.lbWingspan_2.setText(QCoreApplication.translate("Widget", u"Wing", None))
        self.lbWingspan_3.setText(QCoreApplication.translate("Widget", u"Vertical Tail", None))
        self.lbDropDistance.setText(QCoreApplication.translate("Widget", u"Payload drop off distance:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbBWB), QCoreApplication.translate("Widget", u"BWB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbTW), QCoreApplication.translate("Widget", u"Tube And Wing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Mission Parameters", None))
    # retranslateUi

