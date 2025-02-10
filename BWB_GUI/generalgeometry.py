from textprocessingutilities import *
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface

class GeneralGeometry(InternalStorageInterface):
    def __init__(self,
        sweep_deg_wing = None,
        sweep_deg_vertsurf = None,
        sq_ft_wing = None,
        sq_ft_vertsurf = None,
        taper_ratio_wing = None,
        taper_ratio_vertsurf = None,
        aspect_ratio_wing = None,
        aspect_ratio_vertsurf = None,
        tilt_deg = None):
            self.sweep_deg_wing = sweep_deg_wing
            self.sweep_deg_vertsurf = sweep_deg_vertsurf
            self.sq_ft_wing = sq_ft_wing
            self.sq_ft_vertsurf = sq_ft_vertsurf
            self.taper_ratio_wing = taper_ratio_wing
            self.taper_ratio_vertsurf = taper_ratio_vertsurf
            self.aspect_ratio_wing = aspect_ratio_wing
            self.aspect_ratio_vertsurf = aspect_ratio_vertsurf
            self.tilt_deg = tilt_deg

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, value)

    def push_to_dict(self):
        return vars(self)

