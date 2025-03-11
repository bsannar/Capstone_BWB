from aircraft import Aircraft
from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs

class TawGeometry(GeneralGeometry):
    def __init__(self, example_tube_and_wing_var = None):
        super().__init__()
        self.example_tube_and_wing_var = example_tube_and_wing_var

class Taw(Aircraft):
    def __init__(self, name):
        super().__init__(name)
        self.geometry = TawGeometry()
