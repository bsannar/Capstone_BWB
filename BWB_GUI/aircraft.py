from missioninputs import MissionInputs
from missionoutputs import MissionOutputs

class Aircraft:
    def __init__(self, name):
        self.name = name
        self.mission_inputs = MissionInputs()
        self.mission_outputs = MissionOutputs()
        self.has_mission = False

    def list_all_vars(self):
        names = {**vars(self.self.mission_inputs), **vars(self.geometry)}.keys()
        return [convert_from_camel_casing_to_spaces(name) for name in names]

    def list_mission_outputs(self):
        names = vars(self.mission_outputs).keys()
        return [name.replace("_", " ") for name in names]

    def list_mission_inputs(self):
        names = vars(self.mission_inputs).keys()
        return [name.replace("_", " ") for name in names]

    def list_geometry(self):
        names = vars(self.geometry).keys()
        return [name.replace("_", " ") for name in names]
