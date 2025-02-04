from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs

class TawGeometry(GeneralGeometry):
    def __init__(self, example_tube_and_wing_var):
        super().__init__()
        self.example_tube_and_wing_var = None

class Taw:
    def __init__(self, taw_geometry:TawGeometry, mission_parameters: MissionInputs):
        self.geometry = BwbGeometry()
        self.mission_inputs = MissionInputs()

    def list_all_vars(self):
        names = {**vars(self.self.mission_inputs), **vars(self.geometry)}.keys()
        return [convert_from_camel_casing_to_spaces(name) for name in names]
