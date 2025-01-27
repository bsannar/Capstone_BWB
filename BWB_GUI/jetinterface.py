from datainterface import DataInterface
import xlwings as xw
from textprocessingutilities import *

class JetInterface(DataInterface):
    def __init__(self, ui, ui_mission_dict, ui_geometry_dict):
        self.xl = xw.App(visible=True)
        self.wb = self.xl.books.open("Assets/BWB_tanker.xlsm")
        self.main_sheet = self.wb.sheets["Main"]
        self.ui = ui
        self.ui_mission_dict = ui_mission_dict
        self.ui_geometry_dict = ui_geometry_dict
        self.generate_cell_dict()

    def pull_geometry_vars_into_gui(self):
        for key1, val in self.ui_geometry_dict.items():
            if isinstance(val, dict):
                for key2, widget in val.items():
                    widget.setText(str(self.cell_dict[key1][key2].value))
            else:
                val.setText(str(self.cell_dict[key1].value))

    def push_geometry_vars_from_gui(self):
        for key1, val in self.ui_geometry_dict.items():
            if isinstance(val, dict):
                for key2, widget in val.items():
                    self.cell_dict[key1][key2].value = widget.text()
            else:
                self.cell_dict[key1].value = val.text()

        # takeOffWeight = mainSheet["O15"].value
        # dryWeight = mainSheet["O23"].value
        # fuelCapacity = mainSheet["O18"].value
        # specificFuelConsumption = mainSheet["C30"].value

        # bwb = bwb_class.Bwb(bwb_class.BwbJetIndependentVars(wingSqFt, vertTailSqFt, wingAspectRatio, vertTailAspectRatio, wingTaperRatio, vertTailTaperRatio, wingSweep, vertTailSweep,
        #         fuelCapacity, specificFuelConsumption, payloadDropDistance), bwb_class.BwbDependentVars())
        # maxLiftToDragRatio = 0
        # for i in range(26, 47):
        #     liftToDragRatio = performanceSheet['Z'+str(i)].value
        #     if liftToDragRatio > maxLiftToDragRatio:
        #         maxLiftToDragRatio = liftToDragRatio
        # bwb.dependentVars.liftOverDrag = maxLiftToDragRatio
        # bwb.dependentVars.dryWeight = dryWeight
        # get_number_f_35s(bwb, mainSheet)
        # calculate_max_range(bwb, mainSheet)
        # print("Finished")
        # self.wb.app.macro("export_CPACS_file")()
        # self.bwb_configurations_list.append(bwb)

    def pull_mission_vars_into_gui(self):
        pass

    def push_mission_vars_from_gui(self):
        pass

    def close_interface(self):
        self.wb.close()
        self.xl.quit()

    def calculate_lift_over_drag(self):
        pass

    def calculate_f35s_refueled(self):
        pass

    def calculate_max_range(self):
        self.mission_dict["ExpPayload"] = 0
        self.mission_dict["PermPayload"] = 0
        for nautical_miles in range(1, 10000):
            set_payload_drop_distance(mainSheet, nautical_miles*50)
            if mainSheet["X40"].value > mainSheet["O18"].value:
                return (nautical_miles-1)*100

    def calculate_dry_weight(self):
        pass

    def generate_cell_dict(self):
        cell_dict = {"Alt": "33", "Mach": "35", "Dist": "38", "Time": "39", "Payload": "41",
            "TO": "K", "Accel": "L", "Climb1": "M", "Cruise1": "N", "Patrol1": "O", "Service1": "P", "Patrol2": "Q", "Service2": "R", "Patrol3": "S", "Service3": "T", "Climb2": "U", "Cruise2": "V", "Loiter": "W", "Landing": "X",
            "SqFt": "18", "AspectRatio": "19", "TaperRatio": "20", "SweepDeg": "21", "XLocation": "23", "YLocation": "24", "ZLocation": "25", "DihedralDeg": "26",
            "Wing": "B", "Pitchsurf": "C", "Strakes": "D", "Ailerons": "E", "Leadingflaps": "F", "Trailingflaps": "G", "Vertsurf": "H"}
        dict = {}

        # Mission Widgets
        widgets = [self.ui.glDenseMissionParameters.itemAt(i).widget() for i in range(self.ui.glDenseMissionParameters.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = split_camel_casing(name)[-1]
            key2 = ''.join(split_camel_casing(name)[1:-1])
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = self.main_sheet[cell_dict[key2]+cell_dict[key1]]
        dict["ExpPayload"] = self.main_sheet["O17"]
        dict["PermPayload"] = self.main_sheet["O16"]

        #Geometry Widgets
        widgets = [self.ui.glBwbGeometry.itemAt(i).widget() for i in range(self.ui.glBwbGeometry.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = ''.join(split_camel_casing(name)[2:])
            key2 = split_camel_casing(name)[1]
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = self.main_sheet[cell_dict[key2]+cell_dict[key1]]
        dict["TiltDeg"] = self.main_sheet["H27"]

        # Save dictionary to member variable
        self.cell_dict = dict
