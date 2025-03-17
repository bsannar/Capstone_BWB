from aircraft import Aircraft
from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs
from units import U

class BwbGeometry(GeneralGeometry):
    def __init__(self, example_blendedness_var = U(None, '')):
        super().__init__()
        self.example_blendedness_var = example_blendedness_var

class Bwb(Aircraft):
    def __init__(self, name):
        super().__init__(name)
        self.geometry = BwbGeometry()
