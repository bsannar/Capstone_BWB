import xlwings as xw
import openvsp as vsp
import matplotlib.pyplot as plt
from PySide6.QtGui import QPixmap
from bwb_class import BWB
from f_35s_refueled import get_number_f_35s
import numpy as np
import dropdowns
import config_saver as save
import sensitivities as sens
from PySide6.QtWidgets import QFileDialog

class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.xl = xw.App(visible=False)
        self.wb = self.xl.books.open("Assets/BWB_tanker.xlsm")
        self.setupGUI()
        self.connect_all()
        self.bwb_configurations_list = []

    def setupGUI(self):
        mainSheet = self.wb.sheets["Main"]
        self.ui.txtWingSqFt.setText(str(mainSheet["B18"].value))
        self.ui.txtWingAspectRatio.setText(str(mainSheet["B19"].value))
        self.ui.txtWingTaperRatio.setText(str(mainSheet["B20"].value))
        self.ui.txtWingSweep.setText(str(mainSheet["B21"].value))
        self.ui.txtVertTailSqFt.setText(str(mainSheet["H18"].value))
        self.ui.txtVertTailAspectRatio.setText(str(mainSheet["H19"].value))
        self.ui.txtVertTailTaperRatio.setText(str(mainSheet["H20"].value))
        self.ui.txtVertTailSweep.setText(str(mainSheet["H21"].value))
        self.ui.txtDropDistance.setText(str(mainSheet["N38"].value + mainSheet["M38"].value + mainSheet["P38"].value + mainSheet["L38"].value))

    def connect_all(self):
        self.ui.btnPlot.clicked.connect(self.add_plot)
        self.ui.btnUpdate.clicked.connect(self.update_geometry)
        self.ui.actionSave.triggered.connect(self.open_save_dialog)
        self.ui.actionOpen.triggered.connect(self.open_open_dialog)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.btnSensitivities.clicked.connect(lambda: sens.calculate_sensitivity_from_jet(self.bwb_configurations_list[-1], self.wb.sheets["Main"], "B18"))

    def open_save_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Workspace", "", "DST Workspace (*.csv);;All Files (*)")
        if file_path:
            save.class_to_csv(self.bwb_configurations_list, file_path)

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
                dropdowns.setup_dropdown(self.ui.ddMissionParameters, vars(self.bwb_configurations_list[-1]))
            else:
                print("No configurations available to set up dropdown.")


    def open_vsp(self):
        vsp.ReadVSPFile("wing_model.vsp3")
        wing_id = vsp.FindGeom("WingGeom", 0)
        vsp.SetDriverGroup(wing_id, 1, vsp.SPAN_WSECT_DRIVER, vsp.ROOTC_WSECT_DRIVER, vsp.TIPC_WSECT_DRIVER)
        parm_names = vsp.GetGeomParmIDs(wing_id)
        for p in parm_names:
            print("Available parameters for the wing:", vsp.GetParmName(p), ", group:", vsp.GetParmGroupName(p))
        scale_val = self.ui.txtScale.text()
        if scale_val.isdigit:
            vsp.SetParmVal(wing_id, "Scale", "XForm", float(scale_val))
            print("modified")
        vsp.WriteVSPFile("wing_model.vsp3")

    def add_plot(self):
        plotVars = [item.text() for item in self.ui.ddMissionParameters.menu().actions() if item.isChecked()]
        x = np.arange(len(plotVars))
        width = 0.2  # the width of the bars
        multiplier = 0

        size = self.ui.imgPlot.size()
        px = 1/plt.rcParams['figure.dpi']
        plt.figure(figsize=(size.width()*px, size.height()*px))
        fig, ax = plt.subplots(layout='constrained', figsize=(size.width()*px, size.height()*px))

        normalizers = [max([float(vars(bwb)[plotVar]) for bwb in self.bwb_configurations_list]) for plotVar in plotVars]
        values = []
        bar_labels = []
        for i, bwb in enumerate(self.bwb_configurations_list):
            offset = width * multiplier
            labelValues = [float(vars(bwb)[plotVar]) for plotVar in plotVars]
            normalizedValues = [var/norm for var, norm in zip(labelValues, normalizers)]
            rects = ax.bar(x + offset, normalizedValues, width, label="Config "+str(i+1))
            values.extend(labelValues)
            labels = ax.bar_label(rects, rotation=40)
            bar_labels.extend(labels)
            multiplier += 1

        for label, value in zip(bar_labels, values):
            label.set_text(f"{value:.2e}")


        # Add some text for labels, title and custom x-axis tick labels, etc.
        numBWBs = len(self.bwb_configurations_list)
        ax.set_ylabel('Normalized Performance')
        ax.set_title('BWB Performance')
        ax.set_xticks(x + (width * (numBWBs - 1))/2, plotVars, rotation=20)
        ax.legend(bbox_to_anchor=(1, 1), loc='upper left')
        ax.set_ylim(0, 1.2)

        plt.savefig("BWB_performance.png")
        plt.close()
        self.ui.imgPlot.setPixmap(QPixmap("BWB_performance.png"))

    def update_geometry(self):
        print("Updating...")
        mainSheet = self.wb.sheets["Main"]
        weightSheet = self.wb.sheets["Wt"]
        performanceSheet = self.wb.sheets["Perf"]

        wingSqFt = self.ui.txtWingSqFt.text()
        wingAspectRatio = self.ui.txtWingAspectRatio.text()
        wingTaperRatio = self.ui.txtWingTaperRatio.text()
        wingSweep = self.ui.txtWingSweep.text()
        vertTailSqFt = self.ui.txtVertTailSqFt.text()
        vertTailAspectRatio = self.ui.txtVertTailAspectRatio.text()
        vertTailTaperRatio = self.ui.txtVertTailTaperRatio.text()
        vertTailSweep = self.ui.txtVertTailSweep.text()
        payloadDropDistance = float(self.ui.txtDropDistance.text())

        mainSheet["B18"].value = wingSqFt
        mainSheet["B19"].value = wingAspectRatio
        mainSheet["B20"].value = wingTaperRatio
        mainSheet["B21"].value = wingSweep
        mainSheet["H18"].value = vertTailSqFt
        mainSheet["H19"].value = vertTailAspectRatio
        mainSheet["H20"].value = vertTailTaperRatio
        mainSheet["H21"].value = vertTailSweep
        set_payload_drop_distance(mainSheet, payloadDropDistance)

        takeOffWeight = mainSheet["O15"].value
        dryWeight = mainSheet["O23"].value
        fuelCapacity = mainSheet["O18"].value
        specificFuelConsumption = mainSheet["C30"].value
        maxLiftToDragRatio = 0
        for i in range(26, 47):
            liftToDragRatio = performanceSheet['Z'+str(i)].value
            if liftToDragRatio > maxLiftToDragRatio:
                maxLiftToDragRatio = liftToDragRatio

        bwb = BWB(wingSqFt, vertTailSqFt, wingAspectRatio, vertTailAspectRatio, wingTaperRatio, vertTailTaperRatio, wingSweep, vertTailSweep,
                dryWeight, fuelCapacity, specificFuelConsumption, maxLiftToDragRatio, payloadDropDistance)
        get_number_f_35s(bwb, mainSheet)
        calculate_max_range(bwb, mainSheet)
        print("Finished")
        self.bwb_configurations_list.append(bwb)

def set_payload_drop_distance(mainSheet, payloadDropDistance):
    mainSheet["N38"].value = payloadDropDistance - mainSheet["M38"].value - mainSheet["P38"].value - mainSheet["L38"].value

def calculate_max_range(bwb, mainSheet):
    mainSheet["O17"].value = 0
    for nautical_miles in range(1, 10000):
        set_payload_drop_distance(mainSheet, nautical_miles*50)
        if mainSheet["X40"].value > mainSheet["O18"].value:
            bwb.maxRange = (nautical_miles-1)*100
            break
