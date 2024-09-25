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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.addButton = QPushButton(self.tab)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(440, 20, 93, 29))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 113, 26))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 20, 113, 26))
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(320, 20, 111, 31))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 21, 20))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 20, 21, 20))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.insertButton = QPushButton(self.tab_2)
        self.insertButton.setObjectName(u"insertButton")
        self.insertButton.setGeometry(QRect(40, 80, 161, 29))
        self.vspButton = QPushButton(self.tab_2)
        self.vspButton.setObjectName(u"vspButton")
        self.vspButton.setGeometry(QRect(40, 190, 161, 29))
        self.txt_wingspan = QLineEdit(self.tab_2)
        self.txt_wingspan.setObjectName(u"txt_wingspan")
        self.txt_wingspan.setGeometry(QRect(40, 150, 161, 28))
        self.lst_excel = QListWidget(self.tab_2)
        QListWidgetItem(self.lst_excel)
        QListWidgetItem(self.lst_excel)
        QListWidgetItem(self.lst_excel)
        QListWidgetItem(self.lst_excel)
        self.lst_excel.setObjectName(u"lst_excel")
        self.lst_excel.setGeometry(QRect(140, 30, 61, 41))
        self.txt_excel = QLineEdit(self.tab_2)
        self.txt_excel.setObjectName(u"txt_excel")
        self.txt_excel.setGeometry(QRect(40, 30, 91, 28))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.addButton.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"+", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"=", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.insertButton.setText(QCoreApplication.translate("Widget", u"Put text in box", None))
        self.vspButton.setText(QCoreApplication.translate("Widget", u"Set Scale", None))

        __sortingEnabled = self.lst_excel.isSortingEnabled()
        self.lst_excel.setSortingEnabled(False)
        ___qlistwidgetitem = self.lst_excel.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Widget", u"A1", None));
        ___qlistwidgetitem1 = self.lst_excel.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Widget", u"A2", None));
        ___qlistwidgetitem2 = self.lst_excel.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Widget", u"A3", None));
        ___qlistwidgetitem3 = self.lst_excel.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Widget", u"A4", None));
        self.lst_excel.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Tab 2", None))
    # retranslateUi

