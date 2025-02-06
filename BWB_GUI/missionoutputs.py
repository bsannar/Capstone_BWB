from textprocessingutilities import convert_from_camel_casing_to_spaces
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface

class MissionOutputs(InternalStorageInterface):
    def __init__(self,
        fraction_of_remaining_fuel_in_f35s_when_refueled = None,
        payload_transport_distance = None,
        f35s_refueled = None,
        max_range = None):
            self.fraction_of_remaining_fuel_in_f35s_when_refueled = fraction_of_remaining_fuel_in_f35s_when_refueled
            self.payload_transport_distance = payload_transport_distance
            self.f35s_refueled = f35s_refueled
            self.max_range = max_range

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, value)
        print(vars(self))

    def push_to_dict(self):
        pass
