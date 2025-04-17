import os
from win32gui import GetForegroundWindow, GetWindowText
from bwb import Bwb
from taw import Taw
import numpy as np
import dropdowns
import config_saver as save
import sensitivities as sens
from PySide6.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QCheckBox, QSpacerItem, QSizePolicy
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
from responsesurface import ResponseSurface
from loadingbar import LoadingBar

class GuiManager:
    def __init__(self, ui):
        self.ui = ui
        self.bwb_process = QProcess()
        self.taw_process = QProcess()
        self.generate_ui_geometry_dict()
        self.generate_ui_mission_inputs_dict()
        self.jet_bwb_interface = JetInterface("Assets/BWB_benchmarked.xlsm", get_key_structure(self.ui_mission_inputs_dict), get_key_structure(self.ui_geometry_dict))
        self.hasBWBView = False
        self.has_taw_view = False
        self.aircraft_dict = {}
        self.missions_dict = {}
        self.selected_aircraft = Bwb("BWB 1")
        self.tool_gui_manager = DataManager(self.jet_bwb_interface, self)
        self.tool_gui_manager.transfer_geometry_to_output()
        self.jet_taw_interface = JetInterface("Assets/KC-135_benchmarked.xlsm", get_key_structure(self.ui_mission_inputs_dict), get_key_structure(self.ui_geometry_dict))
        self.taw_storage_manager = DataManager(self.jet_taw_interface, self.selected_aircraft)
        self.tool_storage_manager = DataManager(self.jet_bwb_interface, self.selected_aircraft)
        self.gui_storage_manager = DataManager(self, self.selected_aircraft)
        self.csv_interface = CsvInterface()
        self.gui_csv_manager = DataManager(self, self.csv_interface)
        self.csv_tool_manager = DataManager(self.csv_interface, self.jet_bwb_interface)
        self.main_canvas = MatplotlibCanvas(self.ui.widMainPlot)
        self.response_surface_canvas = MatplotlibCanvas(self.ui.widResponseSurface, projection='3d')
        self.setup_all_dropdowns()
        self.generate_check_boxes_from_list_in_layout(self.selected_aircraft.list_mission_outputs(), self.ui.vlMissionOutputs)
        self.log_message("No Aircraft Selected")
        self.connect_all()
        self.ui.txtStepX.setText("4")
        self.ui.txtStepY.setText("4")

    def setup_all_dropdowns(self):
        dropdowns.setup_dropdown(self.ui.ddChooseAircraft, ["KC-135", "C-17", "B-747"])
        dropdowns.setup_dropdown(self.ui.ddChooseMission, ["Tanker", "Airdrop", "Cargo Carry"])
        dropdowns.setup_dropdown(self.ui.ddX, self.selected_aircraft.list_geometry())
        dropdowns.setup_dropdown(self.ui.ddY, self.selected_aircraft.list_geometry())
        dropdowns.setup_dropdown(self.ui.ddZ, self.selected_aircraft.list_mission_outputs())

    def generate_check_boxes_from_list_in_layout(self, list, layout):
        for item in list:
            checkbox = QCheckBox()
            checkbox.setText(item)
            layout.addWidget(checkbox)
        v_spacer = spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(v_spacer)

    def connect_all(self):
        self.ui.btnAddBwbGeometry.clicked.connect(self.add_bwb_geometry)
        self.ui.actionSave.triggered.connect(self.open_save_dialog)
        self.ui.actionOpen.triggered.connect(self.open_open_dialog)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.btnSensitivities.clicked.connect(lambda: sens.calculate_sensitivity_from_jet(self.ui, self.aircraft_dict[-1], self.wb.sheets["Main"], "B18"))
        self.ui.btnViewBWB.clicked.connect(self.open_tigl_viewer)
        self.ui.btnViewAircraftTaw.clicked.connect(self.open_tigl_viewer_taw)
        self.ui.ddChooseMission.menu().triggered.connect(self.on_choose_mission)
        self.ui.ddChooseAircraft.menu().triggered.connect(self.on_choose_aircraft)
        self.ui.btnAddMission.clicked.connect(self.add_mission)
        self.ui.btnSetMission.clicked.connect(self.on_set_mission_clicked)
        self.ui.lwMissions.itemClicked.connect(lambda item: self.set_mission(item.text()))
        self.ui.lwBwbGeometry.itemClicked.connect(lambda item: self.set_selected_bwb(item.text()))
        self.ui.btnPlot.clicked.connect(self.on_btn_plot_clicked)
        self.ui.btnCalculateResponseSurface.clicked.connect(self.generate_response_surface)
        self.ui.btnDeleteBwb.clicked.connect(self.on_btn_delete_bwb_clicked)
        self.ui.ddX.menu().triggered.connect(self.set_response_x)
        self.ui.ddY.menu().triggered.connect(self.set_response_y)
        self.ui.ddZ.menu().triggered.connect(self.set_response_z)

    def on_set_mission_clicked(self):
        for aircraft in LoadingBar.List(list(self.aircraft_dict.values()), message="Assigning Mission..."):
            self.gui_storage_manager.output = aircraft
            self.gui_storage_manager.transfer_mission_inputs_to_output()

    def generate_response_surface(self):
        x_name = [item.text() for item in self.ui.ddX.menu().actions() if item.isChecked()][0]
        y_name = [item.text() for item in self.ui.ddY.menu().actions() if item.isChecked()][0]
        z_name = [item.text() for item in self.ui.ddZ.menu().actions() if item.isChecked()][0]
        self.gui_storage_manager.transfer_mission_inputs_to_output()
        ResponseSurface(self.response_surface_canvas,
                        self.ui.txtMinX.text(),
                        self.ui.txtMaxX.text(),
                        self.ui.txtStepX.text(),
                        self.ui.txtMinY.text(),
                        self.ui.txtMaxY.text(),
                        self.ui.txtStepY.text(),
                        x_name,
                        y_name,
                        z_name,
                        self.selected_aircraft,
                        self.jet_bwb_interface)

    def log_message(self, message):
        """Append messages to the GUI output window instead of the console."""
        self.ui.text_output_taw.setText(message)  # display text value in qlabel

    def on_btn_plot_clicked(self):
        checked_mission_outputs = get_checked_checkboxes_from_layout(self.ui.vlMissionOutputs)
        for aircraft in LoadingBar.List(list(self.aircraft_dict.values()), message="Calculating Performance..."):
            self.tool_storage_manager.output = aircraft
            match aircraft:
                case Taw():
                    self.tool_storage_manager.input = self.jet_taw_interface
                case Bwb():
                    self.tool_storage_manager.input = self.jet_bwb_interface
            for mission_output in checked_mission_outputs:
                match mission_output:
                    case "max f35s refueled":
                        if not aircraft.mission_outputs.max_f35s_refueled.is_calculated:
                            self.tool_storage_manager.transfer_max_f35s_refueled()
                    case "dry weight":
                        if not aircraft.mission_outputs.dry_weight.is_calculated:
                            self.tool_storage_manager.transfer_dry_weight()
                    case "max range":
                        if not aircraft.mission_outputs.max_range.is_calculated:
                            self.tool_storage_manager.transfer_max_range()
                    case "max payload weight":
                        if not aircraft.mission_outputs.max_payload_weight.is_calculated:
                            self.tool_storage_manager.transfer_max_payload_weight()
                    case "cruise lift over drag":
                        if not aircraft.mission_outputs.cruise_lift_over_drag.is_calculated:
                            self.tool_storage_manager.transfer_lift_over_drag()
        self.update_main_plot(checked_mission_outputs)
        self.tool_storage_manager.output = self.selected_aircraft
        self.gui_storage_manager.output = self.selected_aircraft

    def add_bwb_geometry(self):
        self.gui_storage_manager.output = self.selected_aircraft
        self.gui_storage_manager.transfer_geometry_to_output()
        self.gui_storage_manager.transfer_mission_inputs_to_output()
        name = self.ui.txtBwbName.text()
        if name == '':
            name = f"BWB {len(self.aircraft_dict)+1}"
        self.selected_aircraft.name = name
        if name not in self.aircraft_dict:
            self.ui.lwBwbGeometry.addItem(name)
        self.aircraft_dict[name] = copy.deepcopy(self.selected_aircraft)

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
            save.class_to_csv(self.aircraft_dict, file_path)

    def add_mission(self):
        name = self.ui.txtMissionName.text()
        if name == "":
            name = "Mission " + str(self.ui.lwMissions.count()+1)
        self.ui.lwMissions.addItem(name)
        self.gui_storage_manager.transfer_mission_inputs_to_output()
        self.missions_dict[name] = copy.deepcopy(self.selected_aircraft.mission_inputs)

    def save_mission(self):
        self.csv_interface.set_file_path(f"Assets/Missions/{name}.csv")
        self.gui_csv_manager.transfer_mission_inputs_to_output()
        # self.csv_interface.set_file_path(f"Assets/Missions/{mission_name}.csv")
        # self.gui_csv_manager.transfer_mission_inputs_to_input()
        # self.csv_tool_manager.transfer_mission_inputs_to_output()

    def set_mission(self, mission_name):
        clearLayout(self.ui.glMissionParameters)
        self.selected_aircraft.mission_inputs = self.missions_dict[mission_name]
        match self.missions_dict[mission_name].mission_type:
            case missions.Airdrop():
                missions.setup_airdrop_mission(self, self.gui_storage_manager)
            case missions.Tanker():
                missions.setup_tanker_mission(self, self.gui_storage_manager)
            case missions.Cargo():
                missions.setup_cargo_carry_mission(self, self.gui_storage_manager)
            case _:
                print("Default")

    def set_selected_bwb(self, bwb_name):
        self.selected_aircraft = self.aircraft_dict[bwb_name]
        self.ui.txtBwbName.setText(bwb_name)
        self.gui_storage_manager.output = self.selected_aircraft
        self.gui_storage_manager.transfer_geometry_to_input()

    def on_btn_delete_bwb_clicked(self):
        selected_items = self.ui.lwBwbGeometry.selectedItems()
        for item in selected_items:
            self.ui.lwBwbGeometry.takeItem(self.ui.lwBwbGeometry.row(item))
            del self.aircraft_dict[item.text()]

    def open_open_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            new_configs = save.csv_to_class(file_path)
            if new_configs:
                self.aircraft_dict.extend(new_configs)
                print(f"Configurations list updated: {self.aircraft_dict}")
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
                self.log_message("KC-135 selected")
                self.jet_taw_interface.switch_excel("Assets/KC-135_benchmarked.xlsm")
                self.selected_taw_aircraft = Taw('KC-135', self.taw_storage_manager)  # Load TAW aircraft class
                self.jet_taw_interface.generate_cpacs()
                self.tool_storage_manager.input = self.jet_taw_interface
                self.tool_storage_manager.transfer_geometry_to_output()
                self.gui_storage_manager.output = self.selected_taw_aircraft
                self.gui_storage_manager.transfer_mission_inputs_to_output()
                self.aircraft_dict['KC-135'] = copy.deepcopy(self.selected_taw_aircraft)
            case "C-17":
                self.log_message("C-17 selected")
                self.jet_taw_interface.switch_excel("Assets/C-17.xlsm")
                self.selected_taw_aircraft = Taw('C-17', self.taw_storage_manager)  # Load TAW aircraft class
                self.jet_taw_interface.generate_cpacs()
                self.tool_storage_manager.input = self.jet_taw_interface
                self.taw_storage_manager.transfer_geometry_to_output()
                self.taw_storage_manager.transfer_mission_inputs_to_output()
                self.aircraft_dict['C-17'] = copy.deepcopy(self.selected_taw_aircraft)
            case "B-747":
                self.log_message("No B-747 exists in files")
                self.selected_taw_aircraft = Taw('B-747', self.taw_storage_manager)  # Load TAW aircraft class
            case _:
                self.log_message("No aircraft selected")

    def update_main_plot(self, checked_mission_outputs):
        self.main_canvas.ax.cla()
        plotVars = [convert_to_underscores_from_spaces(mission_output) for mission_output in checked_mission_outputs]
        normalize = True
        if len(plotVars) == 0:
            self.main_canvas.draw()
            return
        elif len(plotVars) == 1:
            normalize = False
        x = np.arange(len(plotVars))
        width = 0.2  # the width of the bars
        multiplier = 0

        if normalize:
            normalizers = [max([aircraft.mission_outputs.push_values_to_dict()[plotVar] for aircraft in self.aircraft_dict.values()]) for plotVar in plotVars]
        values = []
        units = []
        bar_labels = []
        all_rects = []
        texts = []
        for name, aircraft in self.aircraft_dict.items():
            value_dict = aircraft.mission_outputs.push_values_to_dict()
            unit_dict = aircraft.mission_outputs.push_units_to_dict()
            texts.append(self.get_unique_geometry(name))
            offset = width * multiplier
            labelValues = [value_dict[plotVar] for plotVar in plotVars]
            label_units = [unit_dict[plotVar] for plotVar in plotVars]
            if normalize:
                normalizedValues = [var/norm for var, norm in zip(labelValues, normalizers)]
                rects = self.main_canvas.ax.bar(x + offset, normalizedValues, width, label=aircraft.name)
            else:
                rects = self.main_canvas.ax.bar(x + offset, labelValues, width, label=aircraft.name)
            units.extend(label_units)
            values.extend(labelValues)
            labels = self.main_canvas.ax.bar_label(rects, rotation=40)
            bar_labels.extend(labels)
            multiplier += 1
            all_rects.append(rects)

        cursor = mplcursors.cursor([rect for rects in all_rects for rect in rects], hover=mplcursors.HoverMode.Transient)
        cursor.connect("add", lambda sel: self.show_annotation(sel, all_rects, texts))

        for label, value, unit in zip(bar_labels, values, units):
            label.set_text(format_number(value)+" "+unit)

        # Add some text for labels, title and custom x-self.main_canvas.axis tick labels, etc.
        n_aircraft = len(self.aircraft_dict)
        if normalize:
            self.main_canvas.ax.set_ylabel('Normalized Performance')
            self.main_canvas.ax.set_ylim(0, 1.25)
        else:
            self.main_canvas.ax.set_ylabel(f'{checked_mission_outputs[0]} ({units[0]})')
            self.main_canvas.ax.set_ylim([0, max(values)*1.25])
        self.main_canvas.ax.set_title('Aircraft Performance')
        self.main_canvas.ax.set_xticks(x + (width * (n_aircraft - 1))/2, [convert_to_spaces_from_underscores(var) for var in plotVars], rotation=20)
        self.main_canvas.ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

        self.main_canvas.draw()

    def show_annotation(self, sel, plots, texts):
        bar = sel.artist
        for i, plot in enumerate(plots):
            if bar in plot:
                idx = i
        sel.annotation.set_text(texts[idx])
        sel.annotation.get_bbox_patch().set(alpha=0.8, fc="white")

    def get_unique_geometry(self, name):
        text_dict = {}
        text = ''
        for _, aircraft in self.aircraft_dict.items():
            geometry = flatten_dict(aircraft.geometry.push_values_to_dict())
            units = flatten_dict(aircraft.geometry.push_units_to_dict())
            for key, value in flatten_dict(self.aircraft_dict[name].geometry.push_values_to_dict()).items():
                if key in geometry:
                    if try_to_float(value) != try_to_float(geometry[key]):
                        new_key = convert_from_camel_casing_to_spaces(key)
                        text_dict[new_key] = f'{value} {units[key]}'
        for key, value in text_dict.items():
            text += f"{key}: {value}\n"
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
            self.log_message("No aircraft selected. Please select an aircraft first.")
            return

        xml_file_map = {
            "KC-135": "Assets/KC-135.xml",
            "C-17": "Assets/C-17.xml",
            "B-747": "Assets/B-747.xml"
        }

        xml_path = xml_file_map.get(self.jet_taw_interface.aircraft_name, None)

        if xml_path is None or not os.path.exists(xml_path):
            self.log_message(f"XML file for {self.selected_taw_aircraft} not found.")
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
        mission_type = [item.text() for item in self.ui.ddChooseMission.menu().actions() if item.isChecked()][0]
        match mission_type:
            case "Airdrop":
                mission_inputs_dict["mission_type"] = missions.Airdrop()
            case "Tanker":
                mission_inputs_dict["mission_type"] = missions.Tanker()
            case "Cargo Carry":
                mission_inputs_dict["mission_type"] = missions.Cargo()
        return mission_inputs_dict

    def pull_mission_inputs_into_gui(self, mission_inputs_dict: dict):
        for key1, dict in self.ui_mission_inputs_dict.items():
            if key1 == "ExpPayload" or key1 == "PermPayload":
                self.ui_mission_inputs_dict[key1].setText(str(mission_inputs_dict[key1]))
            else:
                for key2, val in dict.items():
                    self.ui_mission_inputs_dict[key1][key2].setText(str(mission_inputs_dict[key1][key2]))

    def set_response_x(self):
        name = [item.text() for item in self.ui.ddX.menu().actions() if item.isChecked()][0]
        self.ui.lbResponseXName.setText(name)
        units_dict = flatten_dict(self.selected_aircraft.geometry.push_units_to_dict())
        units_dict = {convert_from_camel_casing_to_underscores(key): unit for key, unit in units_dict.items()}
        unit = units_dict[convert_to_underscores_from_spaces(name)]
        self.ui.lbMinXUnits.setText(unit)
        self.ui.lbMaxXUnits.setText(unit)
        values_dict = flatten_dict(self.selected_aircraft.geometry.push_values_to_dict())
        values_dict = {convert_from_camel_casing_to_underscores(key): value for key, value in values_dict.items()}
        value = values_dict[convert_to_underscores_from_spaces(name)]
        self.ui.txtMinX.setText(f'{0.8*value: 3g}')
        self.ui.txtMaxX.setText(f'{1.2*value: 3g}')

    def set_response_y(self):
        name = [item.text() for item in self.ui.ddY.menu().actions() if item.isChecked()][0]
        self.ui.lbResponseYName.setText(name)
        units_dict = flatten_dict(self.selected_aircraft.geometry.push_units_to_dict())
        units_dict = {convert_from_camel_casing_to_underscores(key): unit for key, unit in units_dict.items()}
        unit = units_dict[convert_to_underscores_from_spaces(name)]
        self.ui.lbMinYUnits.setText(unit)
        self.ui.lbMaxYUnits.setText(unit)
        values_dict = flatten_dict(self.selected_aircraft.geometry.push_values_to_dict())
        values_dict = {convert_from_camel_casing_to_underscores(key): value for key, value in values_dict.items()}
        value = values_dict[convert_to_underscores_from_spaces(name)]
        self.ui.txtMinY.setText(f'{0.8*value: 3g}')
        self.ui.txtMaxY.setText(f'{1.2*value: 3g}')

    def set_response_z(self):
        name = [item.text() for item in self.ui.ddZ.menu().actions() if item.isChecked()][0]
        self.ui.lbResponseZName.setText(name)


