from abc import ABC, abstractmethod

class ToolInterface(ABC):
    @abstractmethod
    def pull_geometry_from_tool(self):
        pass

    @abstractmethod
    def push_geometry_to_tool(self, geometry_dict: dict):
        pass

    @abstractmethod
    def pull_mission_inputs_from_tool(self):
        pass

    @abstractmethod
    def push_mission_inputs_to_tool(self, mission_dict: dict):
        pass

    @abstractmethod
    def close_interface(self):
        pass

    @abstractmethod
    def calculate_dry_weight(self):
        pass

    @abstractmethod
    def calculate_lift_over_drag(self):
        pass

    @abstractmethod
    def calculate_max_payload_weight(self):
        pass

    @abstractmethod
    def calculate_max_f35s_refueled(self):
        pass

    @abstractmethod
    def calculate_max_range(self):
        pass
