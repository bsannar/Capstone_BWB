import xlwings as xw
import openvsp as vsp
import matplotlib.pyplot as plt
import random as rnd
from PySide6.QtGui import QPixmap
from bwb_class import BWB
from f_35s_refueled import get_number_f_35s

class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.setupGUI()
        self.connect_all()

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
        x = []
        y = []
        for i in range(20):
            x.append(i)
            y.append(rnd.uniform(-5, 5))
        size = self.ui.imgPlot.size()
        px = 1/plt.rcParams['figure.dpi']
        plt.figure(figsize=(size.width()*px, size.height()*px))
        plt.scatter(x, y)
        plt.savefig("Scatter_test.png")
        plt.close()
        self.ui.imgPlot.setPixmap(QPixmap("Scatter_test.png"))

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

        mainSheet["B18"].value = wingSqFt
        mainSheet["B19"].value = wingAspectRatio
        mainSheet["B20"].value = wingTaperRatio
        mainSheet["B21"].value = wingSweep
        mainSheet["H18"].value = vertTailSqFt
        mainSheet["H19"].value = vertTailAspectRatio
        mainSheet["H20"].value = vertTailTaperRatio
        mainSheet["H21"].value = vertTailSweep

        takeOffWeight = mainSheet["O15"].value
        dryWeight = weightSheet["B12"].value
        fuelCapacity = takeOffWeight - dryWeight
        specificFuelConsumption = mainSheet["C30"].value
        maxLiftToDragRatio = 0
        for i in range(26, 47):
            liftToDragRatio = performanceSheet['Z'+str(i)].value
            if liftToDragRatio > maxLiftToDragRatio:
                maxLiftToDragRatio = liftToDragRatio
                machNumber = performanceSheet['C'+str(i)].value

        wb.save("new_BWB_tanker.xlsm")
        wb.close()
        xl.quit()
        print("Finished")

        bwb = BWB(wingSqFt, vertTailSqFt, wingAspectRatio, vertTailAspectRatio, wingTaperRatio, vertTailTaperRatio, wingSweep, vertTailSweep,
                dryWeight, fuelCapacity, specificFuelConsumption, maxLiftToDragRatio, machNumber)
        get_number_f_35s(bwb)
        print(bwb.numFighter)
