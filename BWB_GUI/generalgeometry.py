from textprocessingutilities import *
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface
from units import U

class GeneralGeometry(InternalStorageInterface):
    def __init__(self,
        sweep_deg_wing = U(None, '°'),
        sweep_deg_vertsurf = U(None, '°'),
        sq_ft_wing = U(None, 'sq ft'),
        sq_ft_vertsurf = U(None, 'sq ft'),
        taper_ratio_wing = U(None, ''),
        taper_ratio_vertsurf = U(None, ''),
        aspect_ratio_wing = U(None, ''),
        aspect_ratio_vertsurf = U(None, ''),
        tilt_deg = U(None, '°')):
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
            setattr(self, new_key, U(value, vars(self)[new_key].unit))

    def push_to_dict(self):
        dictionary = {}
        for key, value in vars(self).items():
            split_list = [k.capitalize() for k in key.split('_')]
            key1 = ''.join(split_list[:2])
            key2 = split_list[-1]
            if key1 not in dictionary:
                if key1 == "TiltDeg":
                    dictionary[key1] = value.value
                else:
                    dictionary[key1] = {}
                    dictionary[key1][key2] = value.value
            else:
                dictionary[key1][key2] = value.value
        return dictionary

