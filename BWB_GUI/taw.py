from aircraft import Aircraft
from generalgeometry import GeneralGeometry
from missioninputs import MissionInputs
from units import U

class TawGeometry(GeneralGeometry):
    def __init__(self, example_tube_and_wing_var = U(None, '')):
        super().__init__()
        self.example_tube_and_wing_var = example_tube_and_wing_var

class Taw(Aircraft):
    def __init__(self, name, data_manager):
        super().__init__(name)
        self.geometry = TawGeometry()
        data_manager.output = self
        data_manager.transfer_geometry_to_output()
