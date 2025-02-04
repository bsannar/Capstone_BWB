class DataManager:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def transfer_geometry(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from bwb import Bwb
        from taw import Taw

        match self.input:
            case ToolInterface():
                geometry_dict = self.input.pull_geometry_from_tool()
            case GuiManager():
                geometry_dict = self.input.pull_geometry_from_gui()
            case _:
                print("default case")

        match self.output:
            case Bwb():
                self.output.geometry.pull_from_dict(geometry_dict)
            case Taw():
                self.output.geometry.pull_from_dict(geometry_dict)
            case GuiManager():
                self.output.pull_geometry_vars_into_gui(geometry_dict)
            case _:
                print("default case")
