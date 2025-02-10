from toolinterface import ToolInterface
import xlwings as xw
from textprocessingutilities import *

def convert_cell_dict_to_cell_value_dict(cell_dict):
    value_dict = {}
    for key, v in cell_dict.items():
        if isinstance(v, dict):
            value_dict[key] = convert_cell_dict_to_cell_value_dict(v)
        else:
            value_dict[key] = cell_dict[key].value
    return value_dict

class JetInterface(ToolInterface):
    def __init__(self, file_path, mission_keys, geometry_keys):
        self.xl = xw.App(visible=False)
        self.wb = self.xl.books.open(file_path)
        self.main_sheet = self.wb.sheets["Main"]
        self.generate_cell_dicts(mission_keys, geometry_keys)

    def pull_geometry_from_tool(self):
        return convert_cell_dict_to_cell_value_dict(self.geometry_cell_dict)

    def pull_mission_inputs_from_tool(self):
        return convert_cell_dict_to_cell_value_dict(self.mission_cell_dict)

    def push_geometry_to_tool(self, geometry_dict: dict):
        pass

    def push_mission_inputs_to_tool(self, mission_inputs_dict: dict):
        for key1, dict in mission_inputs_dict.items():
            if key1 == "ExpPayload" or key1 == "PermPayload":
                self.mission_cell_dict[key1].value = mission_inputs_dict[key1]
            else:
                for key2, val in dict.items():
                    self.mission_cell_dict[key1][key2].value = mission_inputs_dict[key1][key2]

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

    def close_interface(self):
        self.wb.close()
        self.xl.quit()

    def calculate_lift_over_drag(self):
        pass

    def calculate_f35s_refueled(self):
        pass

    def calculate_max_range(self):
        for nautical_miles in range(1, 10000):
            set_payload_drop_distance(mainSheet, nautical_miles*50)
            if mainSheet["X40"].value > mainSheet["O18"].value:
                return (nautical_miles-1)*100

    def calculate_dry_weight(self):
        pass

    def generate_cell_dicts(self, mission_keys, geometry_keys):
        row_col_dict = {"Alt": "33", "Mach": "35", "Dist": "38", "Time": "39", "Payload": "41",
            "TO": "K", "Accel": "L", "Climb1": "M", "Cruise1": "N", "Patrol1": "O", "Service1": "P", "Patrol2": "Q", "Service2": "R", "Patrol3": "S", "Service3": "T", "Climb2": "U", "Cruise2": "V", "Loiter": "W", "Landing": "X",
            "SqFt": "18", "AspectRatio": "19", "TaperRatio": "20", "SweepDeg": "21", "XLocation": "23", "YLocation": "24", "ZLocation": "25", "DihedralDeg": "26",
            "Wing": "B", "Pitchsurf": "C", "Strakes": "D", "Ailerons": "E", "Leadingflaps": "F", "Trailingflaps": "G", "Vertsurf": "H"}

        mission_dict = {}
        for key in mission_keys:
            if isinstance(key, dict):
                key1, keys2 = list(key.items())[0]
                if key1 not in mission_dict:
                    mission_dict[key1] = {}
                for key2 in keys2:
                    mission_dict[key1][key2] = self.main_sheet[row_col_dict[key2]+row_col_dict[key1]]
        mission_dict["ExpPayload"] = self.main_sheet["O17"]
        mission_dict["PermPayload"] = self.main_sheet["O16"]

        geometry_dict = {}
        for key in geometry_keys:
            if isinstance(key, dict):
                key1, keys2 = list(key.items())[0]
                if key1 not in geometry_dict:
                    geometry_dict[key1] = {}
                for key2 in keys2:
                    geometry_dict[key1][key2] = self.main_sheet[row_col_dict[key2]+row_col_dict[key1]]
        geometry_dict["TiltDeg"] = self.main_sheet["H27"]

        # Save dictionary to member variable
        self.mission_cell_dict = mission_dict
        self.geometry_cell_dict = geometry_dict
