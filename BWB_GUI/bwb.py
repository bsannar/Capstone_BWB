from aircraft import Aircraft
from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs

class BwbGeometry(GeneralGeometry):
    def __init__(self, example_blendedness_var = None):
        super().__init__()
        self.example_blendedness_var = example_blendedness_var

class Bwb(Aircraft):
    def __init__(self):
        super().__init__()
        self.geometry = BwbGeometry()
