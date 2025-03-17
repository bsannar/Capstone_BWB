from textprocessingutilities import convert_from_camel_casing_to_spaces
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface
from units import U

class MissionOutputs(InternalStorageInterface):
    def __init__(self,
        dry_weight = U(None, 'lbs'),
        max_f35s_refueled = U(None, ''),
        max_range = U(None, 'nm'),
        max_payload_weight = U(None, 'lbs')):
            self.dry_weight = dry_weight
            self.max_f35s_refueled = max_f35s_refueled
            self.max_range = max_range
            self.max_payload_weight = max_payload_weight

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, U(value, vars(self)[new_key].unit))

    def push_to_dict(self):
        return {key: var.value for key, var in vars(self).items()}
