class DataManager:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def switch(self):
        input = self.input
        output = self.output
        self.input = output
        self.output = input

    def transfer_geometry_to_input(self):
        self.switch()
        self.transfer_geometry_to_output()
        self.switch()

    def transfer_geometry_to_output(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case ToolInterface():
                geometry_dict = self.input.pull_geometry_from_tool()
            case GuiManager():
                geometry_dict = self.input.pull_geometry_from_gui()
            case Aircraft():
                geometry_dict = self.input.geometry.push_values_to_dict()
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.geometry.pull_from_dict(geometry_dict)
                self.output.mission_outputs.set_all_calculated_bools_to_false()
            case GuiManager():
                self.output.pull_geometry_vars_into_gui(geometry_dict)
            case ToolInterface():
                self.output.push_geometry_to_tool(geometry_dict)
            case _:
                print("default case")

    def transfer_mission_inputs_to_input(self):
        self.switch()
        self.transfer_mission_inputs_to_output()
        self.switch()

    def transfer_mission_inputs_to_output(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft
        from externalstorageinterface import ExternalStorageInterface

        match self.input:
            case Aircraft():
                mission_inputs_dict = self.input.mission_inputs.push_values_to_dict()
            case ToolInterface():
                mission_inputs_dict = self.input.pull_mission_inputs_from_tool()
            case GuiManager():
                mission_inputs_dict = self.input.pull_mission_inputs_from_gui()
            case ExternalStorageInterface():
                mission_inputs_dict = self.input.pull_from_storage()
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_inputs.pull_from_dict(mission_inputs_dict)
                self.output.mission_outputs.set_all_calculated_bools_to_false()
                self.output.has_mission = True
            case GuiManager():
                self.output.pull_mission_inputs_into_gui(mission_inputs_dict)
            case ToolInterface():
                self.output.push_mission_inputs_to_tool(mission_inputs_dict)
            case ExternalStorageInterface():
                self.output.push_to_storage(mission_inputs_dict)
            case _:
                print("default case")

    def transfer_max_range(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case Aircraft():
                mission_outputs_dict = self.input.mission_outputs.push_values_to_dict()
                max_range = mission_outputs_dict["max_range"]
            case ToolInterface():
                self.transfer_geometry_to_input()
                self.transfer_mission_inputs_to_input()
                max_range = self.input.calculate_max_range()
            case GuiManager():
                pass
            case ExternalStorageInterface():
                pass
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_outputs.max_range.value = max_range
                self.output.mission_outputs.max_range.is_calculated = True
            case _:
                print("default case")

    def transfer_max_payload_weight(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case Aircraft():
                mission_outputs_dict = self.input.mission_outputs.push_values_to_dict()
                max_payload_weight = mission_outputs_dict["max_payload_weight"]
            case ToolInterface():
                self.transfer_geometry_to_input()
                self.transfer_mission_inputs_to_input()
                max_payload_weight = self.input.calculate_max_payload_weight()
            case GuiManager():
                pass
            case ExternalStorageInterface():
                pass
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_outputs.max_payload_weight.value = max_payload_weight
                self.output.mission_outputs.max_payload_weight.is_calculated = True
            case _:
                print("default case")

    def transfer_lift_over_drag(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case Aircraft():
                mission_outputs_dict = self.input.mission_outputs.push_values_to_dict()
                cruise_lift_over_drag = mission_outputs_dict["cruise_lift_over_drag"]
            case ToolInterface():
                self.transfer_geometry_to_input()
                self.transfer_mission_inputs_to_input()
                cruise_lift_over_drag = self.input.calculate_lift_over_drag()
            case GuiManager():
                pass
            case ExternalStorageInterface():
                pass
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_outputs.cruise_lift_over_drag.value = cruise_lift_over_drag
                self.output.mission_outputs.cruise_lift_over_drag.is_calculated = True
            case _:
                print("default case")

    def transfer_dry_weight(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case Aircraft():
                mission_outputs_dict = self.input.mission_outputs.push_values_to_dict()
                dry_weight = mission_outputs_dict["dry_weight"]
            case ToolInterface():
                self.transfer_geometry_to_input()
                self.transfer_mission_inputs_to_input()
                dry_weight = self.input.calculate_dry_weight()
            case GuiManager():
                pass
            case ExternalStorageInterface():
                pass
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_outputs.dry_weight.value = dry_weight
                self.output.mission_outputs.dry_weight.is_calculated = True
            case _:
                print("default case")

    def transfer_max_f35s_refueled(self):
        from toolinterface import ToolInterface
        from internalstorageinterface import InternalStorageInterface
        from guimanager import GuiManager
        from aircraft import Aircraft

        match self.input:
            case Aircraft():
                mission_outputs_dict = self.input.mission_outputs.push_values_to_dict()
                max_f35s_refueled = mission_outputs_dict["max_f35s_refueled"]
            case ToolInterface():
                self.transfer_geometry_to_input()
                self.transfer_mission_inputs_to_input()
                max_f35s_refueled = self.input.calculate_max_f35s_refueled()
            case GuiManager():
                pass
            case ExternalStorageInterface():
                pass
            case _:
                print("default case")

        match self.output:
            case Aircraft():
                self.output.mission_outputs.max_f35s_refueled.value = max_f35s_refueled
                self.output.mission_outputs.max_f35s_refueled.is_calculated = True
            case _:
                print("default case")

    def get_output_to_transfer_function_dict(self):
        return {"max_f35s_refueled": self.transfer_max_f35s_refueled,
                "dry_weight": self.transfer_dry_weight,
                "max_range": self.transfer_max_range,
                "max_payload_weight": self.transfer_max_payload_weight,
                "cruise_lift_over_drag": self.transfer_lift_over_drag}

