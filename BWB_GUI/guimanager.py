import matplotlib.pyplot as plt
import os
from win32gui import GetForegroundWindow, GetWindowText
from bwb import Bwb
from f_35s_refueled import get_number_f_35s
import numpy as np
import dropdowns
import config_saver as save
import sensitivities as sens
from PySide6.QtWidgets import QFileDialog, QWidget, QVBoxLayout
from PySide6.QtCore import QProcess
from PySide6.QtGui import QPixmap, QWindow
import missions
from guiutilities import *
from datamanager import DataManager
from textprocessingutilities import *
from jetinterface import JetInterface
import copy

class GuiManager:
    def __init__(self, ui):
        self.ui = ui
        self.process = QProcess()
        self.generate_ui_mission_dict()
        self.generate_ui_geometry_dict()
        self.interface = JetInterface(get_key_structure(self.ui_mission_dict), get_key_structure(self.ui_geometry_dict))
        self.hasBWBView = False
        self.bwb_list = []
        self.loaded_bwb = Bwb()
        self.tool_gui_manager = DataManager(self.interface, self)
        self.tool_gui_manager.transfer_geometry()
        self.tool_storage_manager = DataManager(self.interface, self.loaded_bwb)
        self.gui_storage_manager = DataManager(self, self.loaded_bwb)
        dropdowns.setup_dropdown(self.ui.ddChooseMission, ["Tanker", "Airdrop", "Cargo Carry"], False)
        self.connect_all()

    def connect_all(self):
        self.ui.btnPlot.clicked.connect(self.add_plot)
        self.ui.btnUpdate.clicked.connect(self.update)
        self.ui.actionSave.triggered.connect(self.open_save_dialog)
        self.ui.actionOpen.triggered.connect(self.open_open_dialog)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.btnSensitivities.clicked.connect(lambda: sens.calculate_sensitivity_from_jet(self.ui, self.bwb_list[-1], self.wb.sheets["Main"], "B18"))
        self.ui.btnViewBWB.clicked.connect(self.open_tigl_viewer)
        self.ui.ddChooseMission.menu().triggered.connect(self.on_choose_mission)
        self.ui.btnAddMission.clicked.connect(self.add_mission)
        self.ui.btnSetMission.clicked.connect(lambda: missions.populate_jet(self.ui, self.wb.sheets["Main"]))
        self.ui.lwMissions.itemClicked.connect(lambda item: self.set_mission(item.text()))

    def update(self):
        self.gui_storage_manager.transfer_geometry()
        self.loaded_bwb.mission_inputs.max_range = 1000
        self.bwb_list.append(copy.deepcopy(self.loaded_bwb))

    def pull_geometry_vars_into_gui(self, geometry_dict: dict):
        for key1, val in self.ui_geometry_dict.items():
            if isinstance(val, dict):
                for key2, widget in val.items():
                    widget.setText(str(geometry_dict[key1][key2]))
            else:
                val.setText(str(geometry_dict[key1]))

    def open_save_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            save.class_to_csv(self.bwb_list, file_path)

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
                self.bwb_list.extend(new_configs)
                print(f"Configurations list updated: {self.bwb_list}")
            else:
                print("No configurations loaded from the CSV.")

    def tab_changed(self):
        tabName = self.ui.tabWidget.currentWidget().objectName()
        if tabName == "tbMain":
            if True:
                dropdowns.setup_dropdown(self.ui.ddGeometry, self.loaded_bwb.geometry.list_geometry_vars(), True)
                dropdowns.setup_dropdown(self.ui.ddMissionParameters, self.loaded_bwb.mission_inputs.list_mission_vars(), True)
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
        plotVars = [convert_to_underscores_from_spaces(item.text()) for item in self.ui.ddMissionParameters.menu().actions() if item.isChecked()]
        legendLabels = [item.text() for item in self.ui.ddGeometry.menu().actions() if item.isChecked()]
        x = np.arange(len(plotVars))
        width = 0.2  # the width of the bars
        multiplier = 0

        size = self.ui.imgPlot.size()
        px = 1/plt.rcParams['figure.dpi']
        plt.figure(figsize=(size.width()*px, size.height()*px))
        fig, ax = plt.subplots(layout='constrained', figsize=(size.width()*px, size.height()*px))

        normalizers = [max([float(vars(bwb.mission_inputs)[plotVar]) for bwb in self.bwb_list]) for plotVar in plotVars]
        values = []
        bar_labels = []
        for i, bwb in enumerate(self.bwb_list):
            offset = width * multiplier
            labelValues = [float(vars(bwb.mission_inputs)[plotVar]) for plotVar in plotVars]
            legendLabelValues = [str(vars(bwb.geometry)[convert_to_underscores_from_spaces(legendVar)]) for legendVar in legendLabels]
            normalizedValues = [var/norm for var, norm in zip(labelValues, normalizers)]
            rects = ax.bar(x + offset, normalizedValues, width, label="\n".join([name+": "+format_number(value) for name, value in zip(legendLabels, legendLabelValues)]))
            values.extend(labelValues)
            labels = ax.bar_label(rects, rotation=40)
            bar_labels.extend(labels)
            multiplier += 1

        for label, value in zip(bar_labels, values):
            label.set_text(format_number(value))

        # Add some text for labels, title and custom x-axis tick labels, etc.
        numBWBs = len(self.bwb_list)
        ax.set_ylabel('Normalized Performance')
        ax.set_title('BWB Performance')
        ax.set_xticks(x + (width * (numBWBs - 1))/2, [convert_to_spaces_from_underscores(var) for var in plotVars], rotation=20)
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

    def generate_ui_mission_dict(self):
        dict = {}
        widgets = [self.ui.glDenseMissionParameters.itemAt(i).widget() for i in range(self.ui.glDenseMissionParameters.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = split_camel_casing(name)[-1]
            key2 = ''.join(split_camel_casing(name)[1:-1])
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = w
        dict["ExpPayload"] = self.ui.txtExpendablePayload
        dict["PermPayload"] = self.ui.txtPermanentPayload
        self.ui_mission_dict = dict

    def generate_ui_geometry_dict(self):
        dict = {}
        widgets = [self.ui.glBwbGeometry.itemAt(i).widget() for i in range(self.ui.glBwbGeometry.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = ''.join(split_camel_casing(name)[2:])
            key2 = split_camel_casing(name)[1]
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = w
        #dict["TiltDeg"] = self.ui.txtVertsurfTiltDeg
        self.ui_geometry_dict = dict

    def pull_geometry_from_gui(self):
        geometry_dict = {}
        for key1, val in self.ui_geometry_dict.items():
            if isinstance(val, dict):
                if key1 not in geometry_dict:
                    geometry_dict[key1] = {}
                for key2, widget in val.items():
                    geometry_dict[key1][key2] = widget.text()
            else:
                geometry_dict[key1] = val.text()
        return geometry_dict
