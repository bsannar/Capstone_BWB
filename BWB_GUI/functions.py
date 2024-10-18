import xlwings as xw
import openvsp as vsp
import matplotlib.pyplot as plt
import random as rnd
from PySide6.QtGui import QPixmap
from bwb_class import BWB
from f_35s_refueled import get_number_f_35s
import numpy as np
import dropdowns

class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.setupGUI()
        self.connect_all()
        self.bwb_configurations_list = []

    def setupGUI(self):
        xl = xw.App(visible=False)
        wb = xl.books.open("Assets/BWB_tanker.xlsm")
        mainSheet = wb.sheets["Main"]

        self.ui.txtWingSqFt.setText(str(mainSheet["B18"].value))
        self.ui.txtWingAspectRatio.setText(str(mainSheet["B19"].value))
        self.ui.txtWingTaperRatio.setText(str(mainSheet["B20"].value))
        self.ui.txtWingSweep.setText(str(mainSheet["B21"].value))
        self.ui.txtVertTailSqFt.setText(str(mainSheet["H18"].value))
        self.ui.txtVertTailAspectRatio.setText(str(mainSheet["H19"].value))
        self.ui.txtVertTailTaperRatio.setText(str(mainSheet["H20"].value))
        self.ui.txtVertTailSweep.setText(str(mainSheet["H21"].value))
        self.ui.txtDropDistance.setText(str(mainSheet["N38"].value + mainSheet["M38"].value + mainSheet["P38"].value + mainSheet["L38"].value))

        wb.close()
        xl.quit()

    def connect_all(self):
        self.ui.btnPlot.clicked.connect(self.add_plot)
        self.ui.btnUpdate.clicked.connect(self.update_geometry)

    def add(self):
        txt_one = self.ui.lineEdit.text()
        txt_two = self.ui.lineEdit_2.text()
        if txt_one.isdigit and txt_two.isdigit():
            sum = int(txt_one) + int(txt_two)
            self.ui.textBrowser.setText(str(sum))
        else:
            self.ui.textBrowser.setText("Na")

    def insert(self):

        if len(self.ui.lst_excel.selectedItems()) == 1:
            xl = xw.App(visible=False)
            wb = xl.books.open("test.xlsx")
            mainSheet = wb.mainSheets[0]
            mainSheet[self.ui.lst_excel.selectedItems()[0].text()].value = self.ui.txt_excel.text()
            wb.save("test.xlsx")
            wb.close()
            xl.quit()
        else:
            print("Please select an excel box")

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
        print(plotVars)
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
            labels = ax.bar_label(rects, padding=3)
            bar_labels.extend(labels)
            multiplier += 1

        for label, value in zip(bar_labels, values):
            label.set_text(value)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        numBWBs = len(self.bwb_configurations_list)
        ax.set_ylabel('Normalized Performance')
        ax.set_title('BWB Performance')
        ax.set_xticks(x + (width * (numBWBs - 1))/2, plotVars)
        ax.legend(loc='upper left', ncols=numBWBs)
        ax.set_ylim(0, 1.2)

        plt.savefig("BWB_performance.png")
        plt.close()
        self.ui.imgPlot.setPixmap(QPixmap("BWB_performance.png"))

    def update_geometry(self):
        print("Updating...")
        xl = xw.App(visible=False)
        wb = xl.books.open("Assets/BWB_tanker.xlsm")
        mainSheet = wb.sheets["Main"]
        weightSheet = wb.sheets["Wt"]
        performanceSheet = wb.sheets["Perf"]

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

        wb.close()
        xl.quit()
        print("Finished")
        self.bwb_configurations_list.append(bwb)

        dropdowns.setup_dropdown(self.ui.ddMissionParameters, vars(bwb))

def set_payload_drop_distance(mainSheet, payloadDropDistance):
    mainSheet["N38"].value = payloadDropDistance - mainSheet["M38"].value - mainSheet["P38"].value - mainSheet["L38"].value

def calculate_max_range(bwb, mainSheet):
    mainSheet["O17"].value = 0
    for nautical_miles in range(1, 10000):
        set_payload_drop_distance(mainSheet, nautical_miles*50)
        if mainSheet["X40"].value > mainSheet["O18"].value:
            bwb.maxRange = (nautical_miles-1)*100
            break
