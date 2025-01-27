from abc import ABC, abstractmethod

class DataInterface(ABC):
    @abstractmethod
    def pull_geometry_vars_into_gui(self):
        pass

    @abstractmethod
    def push_geometry_vars_from_gui(self):
        pass

    @abstractmethod
    def pull_mission_vars_into_gui(self):
        pass

    @abstractmethod
    def push_mission_vars_from_gui(self):
        pass

    @abstractmethod
    def calculate_dry_weight(self):
        pass

    @abstractmethod
    def calculate_lift_over_drag(self):
        pass

    @abstractmethod
    def calculate_f35s_refueled(self):
        pass

    @abstractmethod
    def calculate_max_range(self):
        pass

    @abstractmethod
    def close_interface(self):
        pass
