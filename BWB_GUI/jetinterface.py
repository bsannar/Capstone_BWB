from toolinterface import ToolInterface
import xlwings as xw
from textprocessingutilities import *
import os

def convert_cell_dict_to_cell_value_dict(cell_dict):
    value_dict = {}
    for key, v in cell_dict.items():
        if isinstance(v, dict):
            value_dict[key] = convert_cell_dict_to_cell_value_dict(v)
        else:
            value_dict[key] = cell_dict[key].value
    return value_dict

def transfer_dictionary_to_cell_dict(input_dict, cell_dict):
    for key1, val1 in input_dict.items():
        if not isinstance(val1, dict):
            if val1 != None:
                cell_dict[key1].value = val1
        else:
            for key2, val2 in val1.items():
                if val2 != None:
                    cell_dict[key1][key2].value = val2

class JetInterface(ToolInterface):
    def __init__(self, file_path, mission_keys, geometry_keys):
        self.file_path = file_path
        self.aircraft_file_no_extension = file_path.split(".")[0]
        self.aircraft_name = self.aircraft_file_no_extension.split("/")[-1]
        self.xl = xw.App(visible=False)
        self.wb = self.xl.books.open(file_path)
        self.main_sheet = self.wb.sheets["Main"]
        self.generate_cell_dicts(mission_keys, geometry_keys)

    def generate_cpacs(self):

        file_path = self.aircraft_file_no_extension + ".xml"

        if os.path.exists(file_path):  # Check if file exists
            os.remove(file_path)       # Delete the file
            print(f"Deleted old {self.aircraft_name} cpacs file, creating new {self.aircraft_name} cpacs file.")
        else:
            print(f"CPACS file does not currently exist, creating {self.aircraft_name} cpacs file")
        self.wb.app.macro("export_CPACS_file")()
        old_name = "Assets/theAircraft.xml"
        os.rename(old_name, self.aircraft_file_no_extension+".xml")

    def pull_geometry_from_tool(self):
        return convert_cell_dict_to_cell_value_dict(self.geometry_cell_dict)

    def pull_mission_inputs_from_tool(self):
        return convert_cell_dict_to_cell_value_dict(self.mission_cell_dict)

    def push_geometry_to_tool(self, geometry_dict: dict):
        transfer_dictionary_to_cell_dict(geometry_dict, self.geometry_cell_dict)

    def push_mission_inputs_to_tool(self, mission_inputs_dict: dict):
        transfer_dictionary_to_cell_dict(mission_inputs_dict, self.mission_cell_dict)

    def close_interface(self):
        self.wb.close()
        self.xl.quit()

    def calculate_lift_over_drag(self):
        pass

    def calculate_f35s_refueled(self):
        pass

    def set_cruise_distance(self, nautical_miles):
        self.mission_cell_dict["Dist"]["Cruise1"].value = nautical_miles - self.mission_cell_dict["Dist"]["Accel"].value - self.mission_cell_dict["Dist"]["Climb1"].value
        self.mission_cell_dict["Dist"]["Cruise2"].value = nautical_miles - self.mission_cell_dict["Dist"]["Climb2"].value - self.mission_cell_dict["Dist"]["Loiter"].value

    def calculate_max_range(self):
        step = 50
        for nautical_miles in range(step, step*1000, step):
            self.set_cruise_distance(nautical_miles)
            if self.main_sheet["X40"].value > self.main_sheet["O18"].value:
                return (nautical_miles-step)

    def calculate_dry_weight(self):
        pass

    def generate_cell_dicts(self, mission_keys, geometry_keys):
        row_col_dict = {"Alt": "33", "Mach": "35", "Dist": "38", "Time": "39", "Payload": "41",
            "Takeoff": "K", "Accel": "L", "Climb1": "M", "Cruise1": "N", "Patrol1": "O", "Service1": "P", "Patrol2": "Q", "Service2": "R", "Patrol3": "S", "Service3": "T", "Climb2": "U", "Cruise2": "V", "Loiter": "W", "Landing": "X",
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

    def switch_jet_excel(self, file_path):
        if self.file_path != file_path:
            self.file_path = file_path
            self.wb.close()
            self.wb = self.xl.books.open(file_path)
            self.aircraft_file_no_extension = file_path.split(".")[0]
            self.aircraft_name = self.aircraft_file_no_extension.split("/")[-1]

