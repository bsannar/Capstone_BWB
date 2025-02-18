import os
from win32gui import GetForegroundWindow, GetWindowText
from bwb import Bwb
from taw import Taw
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
from csvinterface import CsvInterface
import copy
from matplotlibcanvas import MatplotlibCanvas
import mplcursors

class GuiManager:
    def __init__(self, ui):
        self.ui = ui
        self.bwb_process = QProcess()
        self.taw_process = QProcess()
        self.generate_ui_geometry_dict()
        self.generate_ui_mission_inputs_dict()
        self.jet_bwb_interface = JetInterface("Assets/BWB_tanker.xlsm", get_key_structure(self.ui_mission_inputs_dict), get_key_structure(self.ui_geometry_dict))
        self.hasBWBView = False
        self.has_taw_view = False
        self.aircraft_list = []
        self.loaded_aircraft = Bwb("BWB 1")
        self.tool_gui_manager = DataManager(self.jet_bwb_interface, self)
        self.tool_gui_manager.transfer_geometry_to_output()
        self.jet_taw_interface = JetInterface("Assets/KC-135.xlsm", get_key_structure(self.ui_mission_inputs_dict), get_key_structure(self.ui_geometry_dict))
        self.taw_gui_manager = DataManager(self.jet_taw_interface, self)
        self.taw_storage_manager = DataManager(self.jet_taw_interface, self.loaded_aircraft)
        self.tool_storage_manager = DataManager(self.jet_bwb_interface, self.loaded_aircraft)
        self.gui_storage_manager = DataManager(self, self.loaded_aircraft)
        dropdowns.setup_dropdown(self.ui.ddChooseMission, ["Tanker", "Airdrop", "Cargo Carry"], False)
        self.csv_interface = CsvInterface()
        self.gui_csv_manager = DataManager(self, self.csv_interface)
        self.csv_tool_manager = DataManager(self.csv_interface, self.jet_bwb_interface)
        dropdowns.setup_dropdown(self.ui.ddChooseAircraft, ["KC-135", "C-17", "B-747"], False)
        dropdowns.setup_dropdown(self.ui.ddMissionOutputs, self.loaded_aircraft.list_mission_outputs(), True)
        self.main_canvas = MatplotlibCanvas(self.ui.widMainPlot)
        self.connect_all()

    def connect_all(self):
        self.ui.btnUpdate.clicked.connect(self.update_aircraft_geometry)
        self.ui.actionSave.triggered.connect(self.open_save_dialog)
        self.ui.actionOpen.triggered.connect(self.open_open_dialog)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.btnSensitivities.clicked.connect(lambda: sens.calculate_sensitivity_from_jet(self.ui, self.aircraft_list[-1], self.wb.sheets["Main"], "B18"))
        self.ui.btnViewBWB.clicked.connect(self.open_tigl_viewer)
        self.ui.btnViewAircraftTaw.clicked.connect(self.open_tigl_viewer_taw)
        self.ui.ddChooseMission.menu().triggered.connect(self.on_choose_mission)
        self.ui.ddChooseAircraft.menu().triggered.connect(self.on_choose_aircraft)
        self.ui.btnAddMission.clicked.connect(self.add_mission)
        self.ui.btnSetMission.clicked.connect(self.tool_gui_manager.transfer_mission_inputs_to_input)
        self.ui.lwMissions.itemClicked.connect(lambda item: self.set_mission(item.text()))
        self.ui.ddMissionOutputs.menu().triggered.connect(self.mission_outputs_selected)

    def mission_outputs_selected(self):
        checked_mission_outputs = [item.text() for item in self.ui.ddMissionOutputs.menu().actions() if item.isChecked()]
        for aircraft in self.aircraft_list:
            self.tool_storage_manager.output = aircraft
            self.gui_storage_manager.output = aircraft
            self.gui_storage_manager.transfer_mission_inputs_to_output()
            for mission_output in checked_mission_outputs:
                match mission_output:
                    case "max f35s refueled":
                        self.tool_storage_manager.calculate_f35s_refueled()
                    case "dry weight":
                        pass
                    case "max range":
                        self.tool_storage_manager.transfer_max_range()
                    case "max payload weight":
                        pass
        self.update_main_plot()

    def update_aircraft_geometry(self):
        self.gui_storage_manager.transfer_geometry_to_output()
        self.loaded_aircraft.name = f"Aircraft {len(self.aircraft_list)+1}"
        self.aircraft_list.append(copy.deepcopy(self.loaded_aircraft))

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
            save.class_to_csv(self.aircraft_list, file_path)

    def add_mission(self):
        name = self.ui.txtMissionName.text()
        if name == "":
            name = "Mission " + str(self.ui.lwMissions.count()+1)
        self.ui.lwMissions.addItem(name)
        self.csv_interface.set_file_path(f"Assets/Missions/{name}.csv")
        self.gui_csv_manager.transfer_mission_inputs_to_output()

    def set_mission(self, mission_name):
        self.csv_interface.set_file_path(f"Assets/Missions/{mission_name}.csv")
        self.gui_csv_manager.transfer_mission_inputs_to_input()
        self.csv_tool_manager.transfer_mission_inputs_to_output()

    def open_open_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            new_configs = save.csv_to_class(file_path)
            if new_configs:
                self.aircraft_list.extend(new_configs)
                print(f"Configurations list updated: {self.aircraft_list}")
            else:
                print("No configurations loaded from the CSV.")

    def tab_changed(self):
        tabName = self.ui.tabWidget.currentWidget().objectName()
        if tabName == "tbMain":
            if True:
                pass
            else:
                print("No configurations available to set up dropdown.")

    def on_choose_mission(self):
        clearLayout(self.ui.glMissionParameters)
        match [item.text() for item in self.ui.ddChooseMission.menu().actions() if item.isChecked()][0]:
            case "Tanker":
                missions.setup_tanker_mission(self)
            case "Airdrop":
                missions.setup_airdrop_mission(self)
            case "Cargo Carry":
                missions.setup_cargo_carry_mission(self)
            case _:
                print("No mission selected")

    def on_choose_aircraft(self):
        chosen_aircraft = [item.text() for item in self.ui.ddChooseAircraft.menu().actions() if item.isChecked()][0]

        self.selected_taw_aircraft = chosen_aircraft  # Store the selected aircraft name

        match chosen_aircraft:
            case "KC-135":
                print("KC-135 selected")
                self.jet_taw_interface.switch_excel("Assets/KC-135.xlsm")
                self.selected_taw_aircraft = Taw()  # Load TAW aircraft class
                self.jet_taw_interface.generate_cpacs()
            case "C-17":
                print("C-17 selected")
                self.jet_taw_interface.switch_excel("Assets/C-17.xlsm")
                self.selected_taw_aircraft = Taw()  # Load TAW aircraft class
                self.jet_taw_interface.generate_cpacs()

            case "B-747":
                print("B-747 selected")
                self.selected_taw_aircraft = Taw()  # Load TAW aircraft class
            case _:
                print("No aircraft selected")

    def update_main_plot(self):
        self.main_canvas.ax.cla()
        plotVars = [convert_to_underscores_from_spaces(item.text()) for item in self.ui.ddMissionOutputs.menu().actions() if item.isChecked()]
        if len(plotVars) == 0:
            self.main_canvas.draw()
            return
        x = np.arange(len(plotVars))
        width = 0.2  # the width of the bars
        multiplier = 0

        normalizers = [max([float(vars(aircraft.mission_outputs)[plotVar]) for aircraft in self.aircraft_list]) for plotVar in plotVars]
        values = []
        bar_labels = []
        all_rects = []
        texts = []
        for i, aircraft in enumerate(self.aircraft_list):
            texts.append(self.get_unique_geometry(i))
            offset = width * multiplier
            labelValues = [float(vars(aircraft.mission_outputs)[plotVar]) for plotVar in plotVars]
            normalizedValues = [var/norm for var, norm in zip(labelValues, normalizers)]
            rects = self.main_canvas.ax.bar(x + offset, normalizedValues, width, label=aircraft.name)
            values.extend(labelValues)
            labels = self.main_canvas.ax.bar_label(rects, rotation=40)
            bar_labels.extend(labels)
            multiplier += 1
            all_rects.append(rects)

        cursor = mplcursors.cursor([rect for rects in all_rects for rect in rects], hover=mplcursors.HoverMode.Transient)
        cursor.connect("add", lambda sel: self.show_annotation(sel, all_rects, texts))

        for label, value in zip(bar_labels, values):
            label.set_text(format_number(value))

        # Add some text for labels, title and custom x-self.main_canvas.axis tick labels, etc.
        n_aircraft = len(self.aircraft_list)
        self.main_canvas.ax.set_ylabel('Normalized Performance')
        self.main_canvas.ax.set_title('Aircraft Performance')
        self.main_canvas.ax.set_xticks(x + (width * (n_aircraft - 1))/2, [convert_to_spaces_from_underscores(var) for var in plotVars], rotation=20)
        self.main_canvas.ax.legend(bbox_to_anchor=(1, 1), loc='upper left')
        self.main_canvas.ax.set_ylim(0, 1.2)

        self.main_canvas.draw()

    def show_annotation(self, sel, plots, texts):
        bar = sel.artist
        for i, plot in enumerate(plots):
            if bar in plot:
                idx = i
        sel.annotation.set_text(texts[idx])
        sel.annotation.get_bbox_patch().set(alpha=0.8, fc="white")

    def get_unique_geometry(self, idx):
        text_dict = {}
        text = ''
        for aircraft in self.aircraft_list:
            geometry = flatten_dict(aircraft.geometry.push_to_dict())
            for key, value in flatten_dict(self.aircraft_list[idx].geometry.push_to_dict()).items():
                if value != geometry[key]:
                    text_dict[key] = value
        for key, value in text_dict.items():
            text += f"{convert_from_camel_casing_to_spaces(key)}: {value}\n"
        return text[:-1]

    def open_tigl_viewer(self):
        self.jet_bwb_interface.generate_cpacs()
        if os.path.exists("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe"):
            if not self.hasBWBView:
                self.bwb_process.start("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe", ["Assets/BWB_tanker.xml"])
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

    def open_tigl_viewer_taw(self):
        if not hasattr(self, "selected_taw_aircraft") or not self.jet_taw_interface.aircraft_name:
            print("No aircraft selected. Please select an aircraft first.")
            return

        xml_file_map = {
            "KC-135": "Assets/KC-135.xml",
            "C-17": "Assets/C-17.xml",
            "B-747": "Assets/B-747.xml"
        }

        xml_path = xml_file_map.get(self.jet_taw_interface.aircraft_name, None)

        if xml_path is None or not os.path.exists(xml_path):
            print(f"XML file for {self.selected_taw_aircraft} not found.")
            return

        if os.path.exists("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe"):
            if not self.has_taw_view:
                self.taw_process.start("Executables/TIGL 3.4.0/bin/tiglviewer-3.exe", [xml_path])

                # Wait for the TiGL Viewer window to appear
                title = ""
                while True:
                    hwnd = GetForegroundWindow()
                    title = GetWindowText(hwnd)
                    if title == "TiGL Viewer 3":
                        break

                window = QWindow.fromWinId(hwnd)
                widget = QWidget.createWindowContainer(window)
                layout = QVBoxLayout(self.ui.widTiglTaw)
                layout.addWidget(widget)
                self.ui.widTiglTaw.setLayout(layout)
                self.has_taw_view = True
        else:
            print('The path "Executables/TIGL 3.4.0/bin/tiglviewer-3.exe" does not exist')

    def generate_ui_mission_inputs_dict(self):
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
        self.ui_mission_inputs_dict = dict

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

    def pull_mission_inputs_from_gui(self):
        mission_inputs_dict = {}
        for key1, val in self.ui_mission_inputs_dict.items():
            if isinstance(val, dict):
                if key1 not in mission_inputs_dict:
                    mission_inputs_dict[key1] = {}
                for key2, widget in val.items():
                    mission_inputs_dict[key1][key2] = widget.text()
            else:
                mission_inputs_dict[key1] = val.text()
        return mission_inputs_dict

    def pull_mission_inputs_into_gui(self, mission_inputs_dict: dict):
        for key1, dict in self.ui_mission_inputs_dict.items():
            if key1 == "ExpPayload" or key1 == "PermPayload":
                self.ui_mission_inputs_dict[key1].setText(str(mission_inputs_dict[key1]))
            else:
                for key2, val in dict.items():
                    self.ui_mission_inputs_dict[key1][key2].setText(str(mission_inputs_dict[key1][key2]))
