class DataManager:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def transfer_geometry(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case ToolInterface():
                geometry_dict = self.input.pull_geometry_from_tool()
            case GuiManager():
                geometry_dict = self.input.pull_geometry_from_gui()
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.geometry.pull_from_dict(geometry_dict)
            case GuiManager():
                self.output.pull_geometry_vars_into_gui(geometry_dict)
            case _:
                print("default case")

    def transfer_mission_inputs(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft
        from externalstorageinterface import ExternalStorageInterface

        match self.input:
            case ToolInterface():
                mission_inputs_dict = self.input.pull_mission_inputs_from_tool()
                print(mission_inputs_dict)
            case GuiManager():
                mission_inputs_dict = self.input.pull_mission_inputs_from_gui()
            case ExternalStorageInterface():
                mission_inputs_dict = self.input.pull_from_storage()
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_inputs.pull_from_dict(mission_inputs_dict)
            case GuiManager():
                self.output.pull_mission_inputs_into_gui(mission_inputs_dict)
            case ToolInterface():
                self.output.push_mission_inputs_to_tool(mission_inputs_dict)
            case ExternalStorageInterface():
                self.output.push_to_storage(mission_inputs_dict)
            case _:
                print("default case")
