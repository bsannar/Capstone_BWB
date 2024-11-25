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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 646)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tbMain = QWidget()
        self.tbMain.setObjectName(u"tbMain")
        self.gridLayout_4 = QGridLayout(self.tbMain)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tbMain)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 814, 589))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.imgPlot = QLabel(self.scrollAreaWidgetContents)
        self.imgPlot.setObjectName(u"imgPlot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgPlot.sizePolicy().hasHeightForWidth())
        self.imgPlot.setSizePolicy(sizePolicy)
        self.imgPlot.setPixmap(QPixmap(u"plot_placeholder.png"))

        self.gridLayout_3.addWidget(self.imgPlot, 0, 0, 1, 1)

        self.btnPlot = QPushButton(self.scrollAreaWidgetContents)
        self.btnPlot.setObjectName(u"btnPlot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnPlot.sizePolicy().hasHeightForWidth())
        self.btnPlot.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.btnPlot, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ddGeometry = QToolButton(self.scrollAreaWidgetContents)
        self.ddGeometry.setObjectName(u"ddGeometry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ddGeometry.sizePolicy().hasHeightForWidth())
        self.ddGeometry.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.ddGeometry)

        self.ddMissionParameters = QToolButton(self.scrollAreaWidgetContents)
        self.ddMissionParameters.setObjectName(u"ddMissionParameters")
        sizePolicy2.setHeightForWidth(self.ddMissionParameters.sizePolicy().hasHeightForWidth())
        self.ddMissionParameters.setSizePolicy(sizePolicy2)
        self.ddMissionParameters.setAcceptDrops(False)
        self.ddMissionParameters.setCheckable(False)

        self.verticalLayout.addWidget(self.ddMissionParameters)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tbMain, "")
        self.tbBWB = QWidget()
        self.tbBWB.setObjectName(u"tbBWB")
        self.gridLayout_6 = QGridLayout(self.tbBWB)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.tbBWB)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 831, 582))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbWingspan = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan.setObjectName(u"lbWingspan")

        self.gridLayout.addWidget(self.lbWingspan, 1, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lbDropDistance = QLabel(self.scrollAreaWidgetContents_2)
        self.lbDropDistance.setObjectName(u"lbDropDistance")

        self.gridLayout.addWidget(self.lbDropDistance, 5, 0, 1, 1)

        self.txtVertTailAspectRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertTailAspectRatio.setObjectName(u"txtVertTailAspectRatio")

        self.gridLayout.addWidget(self.txtVertTailAspectRatio, 2, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.txtWingSweep = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingSweep.setObjectName(u"txtWingSweep")

        self.gridLayout.addWidget(self.txtWingSweep, 4, 1, 1, 1)

        self.txtVertTailSweep = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertTailSweep.setObjectName(u"txtVertTailSweep")

        self.gridLayout.addWidget(self.txtVertTailSweep, 4, 2, 1, 1)

        self.txtVertTailTaperRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertTailTaperRatio.setObjectName(u"txtVertTailTaperRatio")

        self.gridLayout.addWidget(self.txtVertTailTaperRatio, 3, 2, 1, 1)

        self.txtDropDistance = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtDropDistance.setObjectName(u"txtDropDistance")

        self.gridLayout.addWidget(self.txtDropDistance, 5, 1, 1, 1)

        self.lbTailspan = QLabel(self.scrollAreaWidgetContents_2)
        self.lbTailspan.setObjectName(u"lbTailspan")

        self.gridLayout.addWidget(self.lbTailspan, 2, 0, 1, 1)

        self.lbWingspan_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan_2.setObjectName(u"lbWingspan_2")

        self.gridLayout.addWidget(self.lbWingspan_2, 0, 1, 1, 1)

        self.txtVertTailSqFt = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertTailSqFt.setObjectName(u"txtVertTailSqFt")

        self.gridLayout.addWidget(self.txtVertTailSqFt, 1, 2, 1, 1)

        self.lbWingspan_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan_3.setObjectName(u"lbWingspan_3")

        self.gridLayout.addWidget(self.lbWingspan_3, 0, 2, 1, 1)

        self.txtWingSqFt = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingSqFt.setObjectName(u"txtWingSqFt")

        self.gridLayout.addWidget(self.txtWingSqFt, 1, 1, 1, 1)

        self.txtWingAspectRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingAspectRatio.setObjectName(u"txtWingAspectRatio")

        self.gridLayout.addWidget(self.txtWingAspectRatio, 2, 1, 1, 1)

        self.txtWingTaperRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingTaperRatio.setObjectName(u"txtWingTaperRatio")

        self.gridLayout.addWidget(self.txtWingTaperRatio, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.btnUpdate = QPushButton(self.scrollAreaWidgetContents_2)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.verticalLayout_3.addWidget(self.btnUpdate)

        self.btnViewBWB = QPushButton(self.scrollAreaWidgetContents_2)
        self.btnViewBWB.setObjectName(u"btnViewBWB")

        self.verticalLayout_3.addWidget(self.btnViewBWB)

        self.widTigl = QWidget(self.scrollAreaWidgetContents_2)
        self.widTigl.setObjectName(u"widTigl")
        sizePolicy.setHeightForWidth(self.widTigl.sizePolicy().hasHeightForWidth())
        self.widTigl.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.widTigl)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tbBWB, "")
        self.tbTW = QWidget()
        self.tbTW.setObjectName(u"tbTW")
        self.tbTW.setEnabled(True)
        self.tabWidget.addTab(self.tbTW, "")
        self.tbMissionParameters = QWidget()
        self.tbMissionParameters.setObjectName(u"tbMissionParameters")
        self.gridLayout_7 = QGridLayout(self.tbMissionParameters)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tblSensitivities = QTableWidget(self.tbMissionParameters)
        self.tblSensitivities.setObjectName(u"tblSensitivities")

        self.gridLayout_7.addWidget(self.tblSensitivities, 0, 0, 1, 1)

        self.btnSensitivities = QPushButton(self.tbMissionParameters)
        self.btnSensitivities.setObjectName(u"btnSensitivities")

        self.gridLayout_7.addWidget(self.btnSensitivities, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tbMissionParameters, "")
        self.tbAssumptions = QWidget()
        self.tbAssumptions.setObjectName(u"tbAssumptions")
        self.tabWidget.addTab(self.tbAssumptions, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BWB Decision Support Tool", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.imgPlot.setText("")
        self.btnPlot.setText(QCoreApplication.translate("MainWindow", u"plot", None))
        self.ddGeometry.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.ddMissionParameters.setText(QCoreApplication.translate("MainWindow", u"Mission Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbMain), QCoreApplication.translate("MainWindow", u"Main", None))
        self.lbWingspan.setText(QCoreApplication.translate("MainWindow", u"Square Footage:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Taper Ratio:", None))
        self.lbDropDistance.setText(QCoreApplication.translate("MainWindow", u"Payload drop off distance:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sweep:", None))
        self.lbTailspan.setText(QCoreApplication.translate("MainWindow", u"Aspect Ratio:", None))
        self.lbWingspan_2.setText(QCoreApplication.translate("MainWindow", u"Wing", None))
        self.lbWingspan_3.setText(QCoreApplication.translate("MainWindow", u"Vertical Tail", None))
        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnViewBWB.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbBWB), QCoreApplication.translate("MainWindow", u"BWB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbTW), QCoreApplication.translate("MainWindow", u"Tube And Wing", None))
        self.btnSensitivities.setText(QCoreApplication.translate("MainWindow", u"Calculate Sensitivities", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbMissionParameters), QCoreApplication.translate("MainWindow", u"Mission Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbAssumptions), QCoreApplication.translate("MainWindow", u"Assumptions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

