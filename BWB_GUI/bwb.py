from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs
from internalstorageinterface import InternalStorageInterface

class BwbGeometry(GeneralGeometry):
    def __init__(self, example_blendedness_var = None):
        super().__init__()
        self.example_blendedness_var = example_blendedness_var

class Bwb():
    def __init__(self):
        self.geometry = BwbGeometry()
        self.mission_inputs = MissionInputs()

    def list_all_vars(self):
        names = {**vars(self.self.mission_inputs), **vars(self.geometry)}.keys()
        return [convert_from_camel_casing_to_spaces(name) for name in names]
