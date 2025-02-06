from aircraft import Aircraft
from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs

class TawGeometry(GeneralGeometry):
    def __init__(self, example_tube_and_wing_var):
        super().__init__()
        self.example_tube_and_wing_var = None

class Taw:
    class Bwb(Aircraft):
        def __init__(self):
            super().__init__()
            self.geometry = TawGeometry()
