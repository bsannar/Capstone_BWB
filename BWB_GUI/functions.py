import xlwings as xw
import openvsp as vsp
import numpy as np
#import calculations/f_35s_refueled as calcs


class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.connect_all()

    def connect_all(self):
        self.ui.addButton.clicked.connect(self.add)
        self.ui.insertButton.clicked.connect(self.insert)
        self.ui.vspButton.clicked.connect(self.open_vsp)

    def add(self):
        txt_one = self.ui.lineEdit.text()
        txt_two = self.ui.lineEdit_2.text()
        if txt_one.isdigit and txt_two.isdigit():
            sum = int(txt_one) + int(txt_two)
            self.ui.textBrowser.setText(str(sum))
        else:
            self.ui.textBrowser.setText('Na')

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
        parm_names = vsp.GetGeomParmIDs(wing_id)
        for p in parm_names:
            print("Available parameters for the wing:", vsp.GetParmName(p), ", group:", vsp.GetParmGroupName(p))
        scale_val = self.ui.txt_wingspan.text()
        if scale_val.isdigit:
            vsp.SetParmVal(wing_id, "Scale", "XForm", float(scale_val))
        vsp.WriteVSPFile("wing_model.vsp3")






