from textprocessingutilities import convert_from_camel_casing_to_spaces
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface

class MissionOutputs(InternalStorageInterface):
    def __init__(self,
        dry_weight = None,
        max_f35s_refueled = None,
        max_range = None,
        max_payload_weight = None):
            self.dry_weight = dry_weight
            self.max_f35s_refueled = max_f35s_refueled
            self.max_range = max_range
            self.max_payload_weight = max_payload_weight

    def get_units(self):
        return {"dry_weight": "lbs",
                "max_f35s_refueled": "",
                "max_range": "nm",
                "max_payload_weight": "lbs"}

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, value)

    def push_to_dict(self):
        pass
