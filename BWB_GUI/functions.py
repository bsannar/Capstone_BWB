#import openvsp as vsp
import matplotlib.pyplot as plt
import os
from win32gui import GetForegroundWindow, GetWindowText
import bwb_class
from f_35s_refueled import get_number_f_35s
import numpy as np
import dropdowns
import config_saver as save
import sensitivities as sens
from PySide6.QtWidgets import QFileDialog, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QWindow
import missions

class Functions():
    def __init__(self, ui, process, interface):
        self.ui = ui
        self.process = process
        self.interface = interface
        self.hasBWBView = False
        self.interface.pull_geometry_vars_into_gui()
        self.bwb_configurations_list = []
        dropdowns.setup_dropdown(self.ui.ddChooseMission, ["Tanker", "Airdrop", "Cargo Carry"], False)
        self.connect_all()

    def connect_all(self):
        self.ui.btnPlot.clicked.connect(self.add_plot)
        self.ui.btnUpdate.clicked.connect(self.interface.push_geometry_vars_from_gui)
        self.ui.actionSave.triggered.connect(self.open_save_dialog)
        self.ui.actionOpen.triggered.connect(self.open_open_dialog)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.btnSensitivities.clicked.connect(lambda: sens.calculate_sensitivity_from_jet(self.ui, self.bwb_configurations_list[-1], self.wb.sheets["Main"], "B18"))
        self.ui.btnViewBWB.clicked.connect(self.open_tigl_viewer)
        self.ui.ddChooseMission.menu().triggered.connect(self.on_choose_mission)
        self.ui.btnAddMission.clicked.connect(self.add_mission)
        self.ui.btnSetMission.clicked.connect(lambda: missions.populate_jet(self.ui, self.wb.sheets["Main"]))
        self.ui.lwMissions.itemClicked.connect(lambda item: self.set_mission(item.text()))

    def open_save_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            save.class_to_csv(self.bwb_configurations_list, file_path)

    def add_mission(self):
        name = self.ui.txtMissionName.text()
        if name == "":
            name = "Mission " + str(self.ui.lwMissions.count()+1)
        self.ui.lwMissions.addItem(name)
        missions.create_mission_csv(self.ui, name)

    def set_mission(self, mission_name):
        missions.populate_ui_from_csv(self.ui, mission_name)
        missions.populate_jet(self.ui, self.wb.sheets["Main"])

    def open_open_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            new_configs = save.csv_to_class(file_path)
            if new_configs:
                self.bwb_configurations_list.extend(new_configs)
                print(f"Configurations list updated: {self.bwb_configurations_list}")
            else:
                print("No configurations loaded from the CSV.")

    def tab_changed(self):
        tabName = self.ui.tabWidget.currentWidget().objectName()
        if tabName == "tbMain":
            if self.bwb_configurations_list:
                dropdowns.setup_dropdown(self.ui.ddGeometry, self.bwb_configurations_list[-1].list_independent_vars(), True)
                dropdowns.setup_dropdown(self.ui.ddMissionParameters, self.bwb_configurations_list[-1].list_dependent_vars(), True)
            else:
                print("No configurations available to set up dropdown.")

    def on_choose_mission(self):
        clearLayout(self.ui.glMissionParameters)
        match [item.text() for item in self.ui.ddChooseMission.menu().actions() if item.isChecked()][0]:
            case "Tanker":
                missions.setup_tanker_mission(self.ui)
            case "Airdrop":
                missions.setup_airdrop_mission(self.ui)
            case "Cargo Carry":
                missions.setup_cargo_carry_mission(self.ui)
            case _:
                print("No mission selected")

    def add_plot(self):
        plotVars = [bwb_class.convert_to_camel_casing(item.text()) for item in self.ui.ddMissionParameters.menu().actions() if item.isChecked()]
        legendLabels = [item.text() for item in self.ui.ddGeometry.menu().actions() if item.isChecked()]
        x = np.arange(len(plotVars))
        width = 0.2  # the width of the bars
        multiplier = 0

        size = self.ui.imgPlot.size()
        px = 1/plt.rcParams['figure.dpi']
        plt.figure(figsize=(size.width()*px, size.height()*px))
        fig, ax = plt.subplots(layout='constrained', figsize=(size.width()*px, size.height()*px))

        normalizers = [max([float(vars(bwb.dependentVars)[plotVar]) for bwb in self.bwb_configurations_list]) for plotVar in plotVars]
        values = []
        bar_labels = []
        for i, bwb in enumerate(self.bwb_configurations_list):
            offset = width * multiplier
            labelValues = [float(vars(bwb.dependentVars)[plotVar]) for plotVar in plotVars]
            legendLabelValues = [str(vars(bwb.independentVars)[bwb_class.convert_to_camel_casing(legendVar)]) for legendVar in legendLabels]
            normalizedValues = [var/norm for var, norm in zip(labelValues, normalizers)]
            rects = ax.bar(x + offset, normalizedValues, width, label="\n".join([name+": "+value for name, value in zip(legendLabels, legendLabelValues)]))
            values.extend(labelValues)
            labels = ax.bar_label(rects, rotation=40)
            bar_labels.extend(labels)
            multiplier += 1

        for label, value in zip(bar_labels, values):
            label.set_text(f"{value:.0f}")


        # Add some text for labels, title and custom x-axis tick labels, etc.
        numBWBs = len(self.bwb_configurations_list)
        ax.set_ylabel('Normalized Performance')
        ax.set_title('BWB Performance')
        ax.set_xticks(x + (width * (numBWBs - 1))/2, [bwb_class.convert_from_camel_casing(var) for var in plotVars], rotation=20)
        ax.legend(bbox_to_anchor=(1, 1), loc='upper left')
        ax.set_ylim(0, 1.2)

        plt.savefig("BWB_performance.png")
        plt.close()
        self.ui.imgPlot.setPixmap(QPixmap("BWB_performance.png"))

    def open_tigl_viewer(self):
        if os.path.exists("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe"):
            if not self.hasBWBView:
                self.process.start("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe", ["Assets/theAircraft.xml"])
                title = ""
                while True:
                    hwnd = GetForegroundWindow()
                    title = GetWindowText(hwnd)
                    if title == "TiGL Viewer 3":
                        break
                window = QWindow.fromWinId(hwnd)
                widget = QWidget.createWindowContainer(window)
                layout = QVBoxLayout(self.ui.widTigl)
                layout.addWidget(widget)
                self.ui.widTigl.setLayout(layout)
                self.hasBWBView = True
        else:
            print('The path "Executables/TIGL 3.4.0/bin/tiglviewer-3.exe" does not exist')

def set_payload_drop_distance(mainSheet, payloadDropDistance):
    mainSheet["N38"].value = payloadDropDistance - mainSheet["M38"].value - mainSheet["P38"].value - mainSheet["L38"].value

def clearLayout(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget():
      child.widget().deleteLater()
