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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 646)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1024, 589))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1041, 582))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.glBwbGeometry = QGridLayout()
        self.glBwbGeometry.setObjectName(u"glBwbGeometry")
        self.lbWingspan_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan_2.setObjectName(u"lbWingspan_2")

        self.glBwbGeometry.addWidget(self.lbWingspan_2, 0, 1, 1, 1)

        self.txtVertsurfSweepDeg = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertsurfSweepDeg.setObjectName(u"txtVertsurfSweepDeg")

        self.glBwbGeometry.addWidget(self.txtVertsurfSweepDeg, 4, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")

        self.glBwbGeometry.addWidget(self.label_6, 4, 0, 1, 1)

        self.txtWingTaperRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingTaperRatio.setObjectName(u"txtWingTaperRatio")

        self.glBwbGeometry.addWidget(self.txtWingTaperRatio, 3, 1, 1, 1)

        self.txtWingAspectRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingAspectRatio.setObjectName(u"txtWingAspectRatio")

        self.glBwbGeometry.addWidget(self.txtWingAspectRatio, 2, 1, 1, 1)

        self.lbWingspan_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan_3.setObjectName(u"lbWingspan_3")

        self.glBwbGeometry.addWidget(self.lbWingspan_3, 0, 2, 1, 1)

        self.txtVertsurfSqFt = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertsurfSqFt.setObjectName(u"txtVertsurfSqFt")

        self.glBwbGeometry.addWidget(self.txtVertsurfSqFt, 1, 2, 1, 1)

        self.txtVertsurfAspectRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertsurfAspectRatio.setObjectName(u"txtVertsurfAspectRatio")

        self.glBwbGeometry.addWidget(self.txtVertsurfAspectRatio, 2, 2, 1, 1)

        self.txtWingSweepDeg = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingSweepDeg.setObjectName(u"txtWingSweepDeg")

        self.glBwbGeometry.addWidget(self.txtWingSweepDeg, 4, 1, 1, 1)

        self.lbWingspan = QLabel(self.scrollAreaWidgetContents_2)
        self.lbWingspan.setObjectName(u"lbWingspan")

        self.glBwbGeometry.addWidget(self.lbWingspan, 1, 0, 1, 1)

        self.txtVertsurfTaperRatio = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtVertsurfTaperRatio.setObjectName(u"txtVertsurfTaperRatio")

        self.glBwbGeometry.addWidget(self.txtVertsurfTaperRatio, 3, 2, 1, 1)

        self.txtWingSqFt = QLineEdit(self.scrollAreaWidgetContents_2)
        self.txtWingSqFt.setObjectName(u"txtWingSqFt")

        self.glBwbGeometry.addWidget(self.txtWingSqFt, 1, 1, 1, 1)

        self.lbTailspan = QLabel(self.scrollAreaWidgetContents_2)
        self.lbTailspan.setObjectName(u"lbTailspan")

        self.glBwbGeometry.addWidget(self.lbTailspan, 2, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.glBwbGeometry.addWidget(self.label_5, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.glBwbGeometry)

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
        self.gridLayout_7.setContentsMargins(0, 11, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ddChooseMission = QToolButton(self.tbMissionParameters)
        self.ddChooseMission.setObjectName(u"ddChooseMission")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ddChooseMission.sizePolicy().hasHeightForWidth())
        self.ddChooseMission.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.ddChooseMission)

        self.glMissionParameters = QGridLayout()
        self.glMissionParameters.setObjectName(u"glMissionParameters")

        self.horizontalLayout.addLayout(self.glMissionParameters)


        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.lwMissions = QListWidget(self.tbMissionParameters)
        self.lwMissions.setObjectName(u"lwMissions")

        self.gridLayout_7.addWidget(self.lwMissions, 9, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.glDenseMissionParameters = QGridLayout()
        self.glDenseMissionParameters.setObjectName(u"glDenseMissionParameters")
        self.label_15 = QLabel(self.tbMissionParameters)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_15, 0, 4, 1, 1)

        self.txtLoiterAlt = QLineEdit(self.tbMissionParameters)
        self.txtLoiterAlt.setObjectName(u"txtLoiterAlt")

        self.glDenseMissionParameters.addWidget(self.txtLoiterAlt, 1, 13, 1, 1)

        self.label_13 = QLabel(self.tbMissionParameters)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_13, 0, 6, 1, 1)

        self.label_17 = QLabel(self.tbMissionParameters)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_17, 0, 2, 1, 1)

        self.txtTOPayload = QLineEdit(self.tbMissionParameters)
        self.txtTOPayload.setObjectName(u"txtTOPayload")

        self.glDenseMissionParameters.addWidget(self.txtTOPayload, 5, 1, 1, 1)

        self.txtService1Alt = QLineEdit(self.tbMissionParameters)
        self.txtService1Alt.setObjectName(u"txtService1Alt")

        self.glDenseMissionParameters.addWidget(self.txtService1Alt, 1, 6, 1, 1)

        self.txtClimb2Time = QLineEdit(self.tbMissionParameters)
        self.txtClimb2Time.setObjectName(u"txtClimb2Time")

        self.glDenseMissionParameters.addWidget(self.txtClimb2Time, 4, 11, 1, 1)

        self.label_4 = QLabel(self.tbMissionParameters)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_4, 0, 12, 1, 1)

        self.txtClimb1Payload = QLineEdit(self.tbMissionParameters)
        self.txtClimb1Payload.setObjectName(u"txtClimb1Payload")

        self.glDenseMissionParameters.addWidget(self.txtClimb1Payload, 5, 3, 1, 1)

        self.label_7 = QLabel(self.tbMissionParameters)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_7, 0, 11, 1, 1)

        self.label_14 = QLabel(self.tbMissionParameters)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_14, 0, 5, 1, 1)

        self.txtService3Dist = QLineEdit(self.tbMissionParameters)
        self.txtService3Dist.setObjectName(u"txtService3Dist")

        self.glDenseMissionParameters.addWidget(self.txtService3Dist, 3, 10, 1, 1)

        self.label_10 = QLabel(self.tbMissionParameters)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_10, 0, 9, 1, 1)

        self.txtLandingPayload = QLineEdit(self.tbMissionParameters)
        self.txtLandingPayload.setObjectName(u"txtLandingPayload")

        self.glDenseMissionParameters.addWidget(self.txtLandingPayload, 5, 14, 1, 1)

        self.txtLoiterMach = QLineEdit(self.tbMissionParameters)
        self.txtLoiterMach.setObjectName(u"txtLoiterMach")

        self.glDenseMissionParameters.addWidget(self.txtLoiterMach, 2, 13, 1, 1)

        self.txtCruise2Dist = QLineEdit(self.tbMissionParameters)
        self.txtCruise2Dist.setObjectName(u"txtCruise2Dist")

        self.glDenseMissionParameters.addWidget(self.txtCruise2Dist, 3, 12, 1, 1)

        self.txtClimb2Dist = QLineEdit(self.tbMissionParameters)
        self.txtClimb2Dist.setObjectName(u"txtClimb2Dist")

        self.glDenseMissionParameters.addWidget(self.txtClimb2Dist, 3, 11, 1, 1)

        self.label_21 = QLabel(self.tbMissionParameters)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)

        self.glDenseMissionParameters.addWidget(self.label_21, 5, 0, 1, 1)

        self.txtPatrol1Time = QLineEdit(self.tbMissionParameters)
        self.txtPatrol1Time.setObjectName(u"txtPatrol1Time")

        self.glDenseMissionParameters.addWidget(self.txtPatrol1Time, 4, 5, 1, 1)

        self.txtService3Alt = QLineEdit(self.tbMissionParameters)
        self.txtService3Alt.setObjectName(u"txtService3Alt")

        self.glDenseMissionParameters.addWidget(self.txtService3Alt, 1, 10, 1, 1)

        self.txtClimb1Alt = QLineEdit(self.tbMissionParameters)
        self.txtClimb1Alt.setObjectName(u"txtClimb1Alt")

        self.glDenseMissionParameters.addWidget(self.txtClimb1Alt, 1, 3, 1, 1)

        self.txtPatrol3Mach = QLineEdit(self.tbMissionParameters)
        self.txtPatrol3Mach.setObjectName(u"txtPatrol3Mach")

        self.glDenseMissionParameters.addWidget(self.txtPatrol3Mach, 2, 9, 1, 1)

        self.txtService1Payload = QLineEdit(self.tbMissionParameters)
        self.txtService1Payload.setObjectName(u"txtService1Payload")

        self.glDenseMissionParameters.addWidget(self.txtService1Payload, 5, 6, 1, 1)

        self.txtCruise2Time = QLineEdit(self.tbMissionParameters)
        self.txtCruise2Time.setObjectName(u"txtCruise2Time")

        self.glDenseMissionParameters.addWidget(self.txtCruise2Time, 4, 12, 1, 1)

        self.txtPatrol3Dist = QLineEdit(self.tbMissionParameters)
        self.txtPatrol3Dist.setObjectName(u"txtPatrol3Dist")

        self.glDenseMissionParameters.addWidget(self.txtPatrol3Dist, 3, 9, 1, 1)

        self.txtAccelTime = QLineEdit(self.tbMissionParameters)
        self.txtAccelTime.setObjectName(u"txtAccelTime")

        self.glDenseMissionParameters.addWidget(self.txtAccelTime, 4, 2, 1, 1)

        self.txtService1Dist = QLineEdit(self.tbMissionParameters)
        self.txtService1Dist.setObjectName(u"txtService1Dist")

        self.glDenseMissionParameters.addWidget(self.txtService1Dist, 3, 6, 1, 1)

        self.txtCruise2Alt = QLineEdit(self.tbMissionParameters)
        self.txtCruise2Alt.setObjectName(u"txtCruise2Alt")

        self.glDenseMissionParameters.addWidget(self.txtCruise2Alt, 1, 12, 1, 1)

        self.txtService3Payload = QLineEdit(self.tbMissionParameters)
        self.txtService3Payload.setObjectName(u"txtService3Payload")

        self.glDenseMissionParameters.addWidget(self.txtService3Payload, 5, 10, 1, 1)

        self.txtService2Payload = QLineEdit(self.tbMissionParameters)
        self.txtService2Payload.setObjectName(u"txtService2Payload")

        self.glDenseMissionParameters.addWidget(self.txtService2Payload, 5, 8, 1, 1)

        self.txtCruise1Dist = QLineEdit(self.tbMissionParameters)
        self.txtCruise1Dist.setObjectName(u"txtCruise1Dist")

        self.glDenseMissionParameters.addWidget(self.txtCruise1Dist, 3, 4, 1, 1)

        self.txtPatrol1Payload = QLineEdit(self.tbMissionParameters)
        self.txtPatrol1Payload.setObjectName(u"txtPatrol1Payload")

        self.glDenseMissionParameters.addWidget(self.txtPatrol1Payload, 5, 5, 1, 1)

        self.txtClimb2Payload = QLineEdit(self.tbMissionParameters)
        self.txtClimb2Payload.setObjectName(u"txtClimb2Payload")

        self.glDenseMissionParameters.addWidget(self.txtClimb2Payload, 5, 11, 1, 1)

        self.txtCruise2Mach = QLineEdit(self.tbMissionParameters)
        self.txtCruise2Mach.setObjectName(u"txtCruise2Mach")

        self.glDenseMissionParameters.addWidget(self.txtCruise2Mach, 2, 12, 1, 1)

        self.txtPatrol1Alt = QLineEdit(self.tbMissionParameters)
        self.txtPatrol1Alt.setObjectName(u"txtPatrol1Alt")

        self.glDenseMissionParameters.addWidget(self.txtPatrol1Alt, 1, 5, 1, 1)

        self.txtAccelAlt = QLineEdit(self.tbMissionParameters)
        self.txtAccelAlt.setObjectName(u"txtAccelAlt")

        self.glDenseMissionParameters.addWidget(self.txtAccelAlt, 1, 2, 1, 1)

        self.txtLandingTime = QLineEdit(self.tbMissionParameters)
        self.txtLandingTime.setObjectName(u"txtLandingTime")

        self.glDenseMissionParameters.addWidget(self.txtLandingTime, 4, 14, 1, 1)

        self.txtService2Mach = QLineEdit(self.tbMissionParameters)
        self.txtService2Mach.setObjectName(u"txtService2Mach")

        self.glDenseMissionParameters.addWidget(self.txtService2Mach, 2, 8, 1, 1)

        self.label_2 = QLabel(self.tbMissionParameters)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_2, 0, 14, 1, 1)

        self.txtService2Time = QLineEdit(self.tbMissionParameters)
        self.txtService2Time.setObjectName(u"txtService2Time")

        self.glDenseMissionParameters.addWidget(self.txtService2Time, 4, 8, 1, 1)

        self.label_12 = QLabel(self.tbMissionParameters)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_12, 0, 7, 1, 1)

        self.txtLoiterPayload = QLineEdit(self.tbMissionParameters)
        self.txtLoiterPayload.setObjectName(u"txtLoiterPayload")

        self.glDenseMissionParameters.addWidget(self.txtLoiterPayload, 5, 13, 1, 1)

        self.txtClimb2Mach = QLineEdit(self.tbMissionParameters)
        self.txtClimb2Mach.setObjectName(u"txtClimb2Mach")

        self.glDenseMissionParameters.addWidget(self.txtClimb2Mach, 2, 11, 1, 1)

        self.txtPatrol2Time = QLineEdit(self.tbMissionParameters)
        self.txtPatrol2Time.setObjectName(u"txtPatrol2Time")

        self.glDenseMissionParameters.addWidget(self.txtPatrol2Time, 4, 7, 1, 1)

        self.txtClimb1Mach = QLineEdit(self.tbMissionParameters)
        self.txtClimb1Mach.setObjectName(u"txtClimb1Mach")

        self.glDenseMissionParameters.addWidget(self.txtClimb1Mach, 2, 3, 1, 1)

        self.txtPatrol2Mach = QLineEdit(self.tbMissionParameters)
        self.txtPatrol2Mach.setObjectName(u"txtPatrol2Mach")

        self.glDenseMissionParameters.addWidget(self.txtPatrol2Mach, 2, 7, 1, 1)

        self.txtClimb1Dist = QLineEdit(self.tbMissionParameters)
        self.txtClimb1Dist.setObjectName(u"txtClimb1Dist")

        self.glDenseMissionParameters.addWidget(self.txtClimb1Dist, 3, 3, 1, 1)

        self.txtLandingAlt = QLineEdit(self.tbMissionParameters)
        self.txtLandingAlt.setObjectName(u"txtLandingAlt")

        self.glDenseMissionParameters.addWidget(self.txtLandingAlt, 1, 14, 1, 1)

        self.label_18 = QLabel(self.tbMissionParameters)
        self.label_18.setObjectName(u"label_18")

        self.glDenseMissionParameters.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_20 = QLabel(self.tbMissionParameters)
        self.label_20.setObjectName(u"label_20")

        self.glDenseMissionParameters.addWidget(self.label_20, 4, 0, 1, 1)

        self.txtService1Time = QLineEdit(self.tbMissionParameters)
        self.txtService1Time.setObjectName(u"txtService1Time")

        self.glDenseMissionParameters.addWidget(self.txtService1Time, 4, 6, 1, 1)

        self.txtTODist = QLineEdit(self.tbMissionParameters)
        self.txtTODist.setObjectName(u"txtTODist")

        self.glDenseMissionParameters.addWidget(self.txtTODist, 3, 1, 1, 1)

        self.txtLoiterTime = QLineEdit(self.tbMissionParameters)
        self.txtLoiterTime.setObjectName(u"txtLoiterTime")

        self.glDenseMissionParameters.addWidget(self.txtLoiterTime, 4, 13, 1, 1)

        self.txtAccelMach = QLineEdit(self.tbMissionParameters)
        self.txtAccelMach.setObjectName(u"txtAccelMach")

        self.glDenseMissionParameters.addWidget(self.txtAccelMach, 2, 2, 1, 1)

        self.txtService2Alt = QLineEdit(self.tbMissionParameters)
        self.txtService2Alt.setObjectName(u"txtService2Alt")

        self.glDenseMissionParameters.addWidget(self.txtService2Alt, 1, 8, 1, 1)

        self.txtCruise1Mach = QLineEdit(self.tbMissionParameters)
        self.txtCruise1Mach.setObjectName(u"txtCruise1Mach")

        self.glDenseMissionParameters.addWidget(self.txtCruise1Mach, 2, 4, 1, 1)

        self.txtPatrol3Time = QLineEdit(self.tbMissionParameters)
        self.txtPatrol3Time.setObjectName(u"txtPatrol3Time")

        self.glDenseMissionParameters.addWidget(self.txtPatrol3Time, 4, 9, 1, 1)

        self.txtCruise2Payload = QLineEdit(self.tbMissionParameters)
        self.txtCruise2Payload.setObjectName(u"txtCruise2Payload")

        self.glDenseMissionParameters.addWidget(self.txtCruise2Payload, 5, 12, 1, 1)

        self.txtCruise1Payload = QLineEdit(self.tbMissionParameters)
        self.txtCruise1Payload.setObjectName(u"txtCruise1Payload")

        self.glDenseMissionParameters.addWidget(self.txtCruise1Payload, 5, 4, 1, 1)

        self.txtTOMach = QLineEdit(self.tbMissionParameters)
        self.txtTOMach.setObjectName(u"txtTOMach")

        self.glDenseMissionParameters.addWidget(self.txtTOMach, 2, 1, 1, 1)

        self.txtCruise1Alt = QLineEdit(self.tbMissionParameters)
        self.txtCruise1Alt.setObjectName(u"txtCruise1Alt")

        self.glDenseMissionParameters.addWidget(self.txtCruise1Alt, 1, 4, 1, 1)

        self.txtClimb1Time = QLineEdit(self.tbMissionParameters)
        self.txtClimb1Time.setObjectName(u"txtClimb1Time")

        self.glDenseMissionParameters.addWidget(self.txtClimb1Time, 4, 3, 1, 1)

        self.label_9 = QLabel(self.tbMissionParameters)
        self.label_9.setObjectName(u"label_9")

        self.glDenseMissionParameters.addWidget(self.label_9, 2, 0, 1, 1)

        self.txtPatrol1Dist = QLineEdit(self.tbMissionParameters)
        self.txtPatrol1Dist.setObjectName(u"txtPatrol1Dist")

        self.glDenseMissionParameters.addWidget(self.txtPatrol1Dist, 3, 5, 1, 1)

        self.txtTOAlt = QLineEdit(self.tbMissionParameters)
        self.txtTOAlt.setObjectName(u"txtTOAlt")

        self.glDenseMissionParameters.addWidget(self.txtTOAlt, 1, 1, 1, 1)

        self.txtService2Dist = QLineEdit(self.tbMissionParameters)
        self.txtService2Dist.setObjectName(u"txtService2Dist")

        self.glDenseMissionParameters.addWidget(self.txtService2Dist, 3, 8, 1, 1)

        self.txtLoiterDist = QLineEdit(self.tbMissionParameters)
        self.txtLoiterDist.setObjectName(u"txtLoiterDist")

        self.glDenseMissionParameters.addWidget(self.txtLoiterDist, 3, 13, 1, 1)

        self.txtClimb2Alt = QLineEdit(self.tbMissionParameters)
        self.txtClimb2Alt.setObjectName(u"txtClimb2Alt")

        self.glDenseMissionParameters.addWidget(self.txtClimb2Alt, 1, 11, 1, 1)

        self.txtPatrol2Dist = QLineEdit(self.tbMissionParameters)
        self.txtPatrol2Dist.setObjectName(u"txtPatrol2Dist")

        self.glDenseMissionParameters.addWidget(self.txtPatrol2Dist, 3, 7, 1, 1)

        self.txtPatrol3Alt = QLineEdit(self.tbMissionParameters)
        self.txtPatrol3Alt.setObjectName(u"txtPatrol3Alt")

        self.glDenseMissionParameters.addWidget(self.txtPatrol3Alt, 1, 9, 1, 1)

        self.label_8 = QLabel(self.tbMissionParameters)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_8, 0, 13, 1, 1)

        self.txtAccelDist = QLineEdit(self.tbMissionParameters)
        self.txtAccelDist.setObjectName(u"txtAccelDist")

        self.glDenseMissionParameters.addWidget(self.txtAccelDist, 3, 2, 1, 1)

        self.txtService3Time = QLineEdit(self.tbMissionParameters)
        self.txtService3Time.setObjectName(u"txtService3Time")

        self.glDenseMissionParameters.addWidget(self.txtService3Time, 4, 10, 1, 1)

        self.txtPatrol2Alt = QLineEdit(self.tbMissionParameters)
        self.txtPatrol2Alt.setObjectName(u"txtPatrol2Alt")

        self.glDenseMissionParameters.addWidget(self.txtPatrol2Alt, 1, 7, 1, 1)

        self.txtPatrol2Payload = QLineEdit(self.tbMissionParameters)
        self.txtPatrol2Payload.setObjectName(u"txtPatrol2Payload")

        self.glDenseMissionParameters.addWidget(self.txtPatrol2Payload, 5, 7, 1, 1)

        self.label_11 = QLabel(self.tbMissionParameters)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_11, 0, 8, 1, 1)

        self.txtLandingDist = QLineEdit(self.tbMissionParameters)
        self.txtLandingDist.setObjectName(u"txtLandingDist")

        self.glDenseMissionParameters.addWidget(self.txtLandingDist, 3, 14, 1, 1)

        self.txtAccelPayload = QLineEdit(self.tbMissionParameters)
        self.txtAccelPayload.setObjectName(u"txtAccelPayload")

        self.glDenseMissionParameters.addWidget(self.txtAccelPayload, 5, 2, 1, 1)

        self.lbService3 = QLabel(self.tbMissionParameters)
        self.lbService3.setObjectName(u"lbService3")
        self.lbService3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.lbService3, 0, 10, 1, 1)

        self.txtCruise1Time = QLineEdit(self.tbMissionParameters)
        self.txtCruise1Time.setObjectName(u"txtCruise1Time")

        self.glDenseMissionParameters.addWidget(self.txtCruise1Time, 4, 4, 1, 1)

        self.txtTOTime = QLineEdit(self.tbMissionParameters)
        self.txtTOTime.setObjectName(u"txtTOTime")

        self.glDenseMissionParameters.addWidget(self.txtTOTime, 4, 1, 1, 1)

        self.txtPatrol1Mach = QLineEdit(self.tbMissionParameters)
        self.txtPatrol1Mach.setObjectName(u"txtPatrol1Mach")

        self.glDenseMissionParameters.addWidget(self.txtPatrol1Mach, 2, 5, 1, 1)

        self.label_3 = QLabel(self.tbMissionParameters)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_3, 0, 1, 1, 1)

        self.txtService1Mach = QLineEdit(self.tbMissionParameters)
        self.txtService1Mach.setObjectName(u"txtService1Mach")

        self.glDenseMissionParameters.addWidget(self.txtService1Mach, 2, 6, 1, 1)

        self.txtPatrol3Payload = QLineEdit(self.tbMissionParameters)
        self.txtPatrol3Payload.setObjectName(u"txtPatrol3Payload")

        self.glDenseMissionParameters.addWidget(self.txtPatrol3Payload, 5, 9, 1, 1)

        self.txtLandingMach = QLineEdit(self.tbMissionParameters)
        self.txtLandingMach.setObjectName(u"txtLandingMach")

        self.glDenseMissionParameters.addWidget(self.txtLandingMach, 2, 14, 1, 1)

        self.label_19 = QLabel(self.tbMissionParameters)
        self.label_19.setObjectName(u"label_19")

        self.glDenseMissionParameters.addWidget(self.label_19, 3, 0, 1, 1)

        self.txtService3Mach = QLineEdit(self.tbMissionParameters)
        self.txtService3Mach.setObjectName(u"txtService3Mach")

        self.glDenseMissionParameters.addWidget(self.txtService3Mach, 2, 10, 1, 1)

        self.label_16 = QLabel(self.tbMissionParameters)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glDenseMissionParameters.addWidget(self.label_16, 0, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.glDenseMissionParameters)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_23 = QLabel(self.tbMissionParameters)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_5.addWidget(self.label_23)

        self.txtPermanentPayload = QLineEdit(self.tbMissionParameters)
        self.txtPermanentPayload.setObjectName(u"txtPermanentPayload")

        self.verticalLayout_5.addWidget(self.txtPermanentPayload)

        self.label_24 = QLabel(self.tbMissionParameters)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_5.addWidget(self.label_24)

        self.txtExpendablePayload = QLineEdit(self.tbMissionParameters)
        self.txtExpendablePayload.setObjectName(u"txtExpendablePayload")

        self.verticalLayout_5.addWidget(self.txtExpendablePayload)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_22 = QLabel(self.tbMissionParameters)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_2.addWidget(self.label_22)

        self.txtMissionName = QLineEdit(self.tbMissionParameters)
        self.txtMissionName.setObjectName(u"txtMissionName")

        self.horizontalLayout_2.addWidget(self.txtMissionName)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_7.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.btnAddMission = QPushButton(self.tbMissionParameters)
        self.btnAddMission.setObjectName(u"btnAddMission")

        self.gridLayout_7.addWidget(self.btnAddMission, 8, 0, 1, 1)

        self.btnSetMission = QPushButton(self.tbMissionParameters)
        self.btnSetMission.setObjectName(u"btnSetMission")

        self.gridLayout_7.addWidget(self.btnSetMission, 10, 0, 1, 1)

        self.tabWidget.addTab(self.tbMissionParameters, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tblSensitivities = QTableWidget(self.tab)
        self.tblSensitivities.setObjectName(u"tblSensitivities")

        self.gridLayout_2.addWidget(self.tblSensitivities, 0, 0, 1, 1)

        self.btnSensitivities = QPushButton(self.tab)
        self.btnSensitivities.setObjectName(u"btnSensitivities")

        self.gridLayout_2.addWidget(self.btnSensitivities, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tbAssumptions = QWidget()
        self.tbAssumptions.setObjectName(u"tbAssumptions")
        self.tabWidget.addTab(self.tbAssumptions, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1047, 25))
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
        self.lbWingspan_2.setText(QCoreApplication.translate("MainWindow", u"Wing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sweep:", None))
        self.lbWingspan_3.setText(QCoreApplication.translate("MainWindow", u"Vertical Surface", None))
        self.lbWingspan.setText(QCoreApplication.translate("MainWindow", u"Square Footage:", None))
        self.lbTailspan.setText(QCoreApplication.translate("MainWindow", u"Aspect Ratio:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Taper Ratio:", None))
        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnViewBWB.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbBWB), QCoreApplication.translate("MainWindow", u"BWB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbTW), QCoreApplication.translate("MainWindow", u"Tube And Wing", None))
        self.ddChooseMission.setText(QCoreApplication.translate("MainWindow", u"Choose Mission", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cruise1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Service1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Accel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cruise2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Climb2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Patrol1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Patrol3", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Drop Payload (lb)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Landing", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Patrol2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Altitude (ft)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Time (min)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mach Number", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Loiter", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Service2", None))
        self.lbService3.setText(QCoreApplication.translate("MainWindow", u"Service3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"STTO", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Distance (nm)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Climb1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Permanent Payload", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Expendable Payload", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.btnAddMission.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnSetMission.setText(QCoreApplication.translate("MainWindow", u"Set Mission", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbMissionParameters), QCoreApplication.translate("MainWindow", u"Mission Parameters", None))
        self.btnSensitivities.setText(QCoreApplication.translate("MainWindow", u"Calculate Sensitivities", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Sensitivities", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbAssumptions), QCoreApplication.translate("MainWindow", u"Assumptions", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

