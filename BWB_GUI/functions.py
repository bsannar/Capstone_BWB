import xlwings as xw
import openvsp as vsp
import matplotlib.pyplot as plt
import random as rnd
from PySide6.QtGui import QPixmap

class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.wingspan = False
        self.tailspan = False
        self.connect_all()

    def connect_all(self):
        self.ui.addButton.clicked.connect(self.add)
        self.ui.insertButton.clicked.connect(self.insert)
        self.ui.btnVSP.clicked.connect(self.open_vsp)
        self.ui.btnPlot.clicked.connect(self.add_plot)
        self.ui.txtWingspan.editingFinished.connect(self.set_wingspan)
        self.ui.txtTailspan.editingFinished.connect(self.set_tailspan)
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
            sheet = wb.sheets[0]
            sheet[self.ui.lst_excel.selectedItems()[0].text()].value = self.ui.txt_excel.text()
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
        sheet = wb.sheets["Main"]
        if self.wingspan:
            sheet["B18"].value = self.ui.txtWingspan.text()
        if self.tailspan:
            sheet["H18"].value = self.ui.txtTailspan.text()
        wb.save("new_BWB_tanker.xlsm")
        wb.close()
        xl.quit()
        print("Finished")
