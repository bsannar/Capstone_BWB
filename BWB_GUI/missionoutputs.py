from textprocessingutilities import convert_from_camel_casing_to_spaces
from guiutilities import flatten_dict, try_to_float
from internalstorageinterface import InternalStorageInterface
from units import U

class MissionOutputs(InternalStorageInterface):
    def __init__(self,
        dry_weight = U(None, 'lbs'),
        max_f35s_refueled = U(None, ''),
        max_range = U(None, 'nm'),
        max_payload_weight = U(None, 'lbs'),
        cruise_lift_over_drag = U(None, '')):
            self.dry_weight = dry_weight
            self.max_f35s_refueled = max_f35s_refueled
            self.max_range = max_range
            self.max_payload_weight = max_payload_weight
            self.cruise_lift_over_drag = cruise_lift_over_drag

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, U(try_to_float(value), vars(self)[new_key].unit))

    def push_values_to_dict(self):
        return {key: try_to_float(var.value) for key, var in vars(self).items()}

    def push_units_to_dict(self):
        return {key: var.unit for key, var in vars(self).items()}

    def set_all_calculated_bools_to_false(self):
        for key, var in vars(self).items():
            var.is_calculated = False
