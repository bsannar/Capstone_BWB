from textprocessingutilities import *
from guiutilities import flatten_dict, try_to_float
from internalstorageinterface import InternalStorageInterface
from units import U

class GeneralGeometry(InternalStorageInterface):
    def __init__(self,
        sweep_deg_wing = U(None, '°'),
        sweep_deg_pitchctrl = U(None, '°'),
        sweep_deg_strakes = U(None, '°'),
        sweep_deg_ailerons = U(None, '°'),
        sweep_deg_leadingflaps = U(None, '°'),
        sweep_deg_trailingflaps = U(None, '°'),
        sweep_deg_vertsurf = U(None, '°'),
        sq_ft_wing = U(None, 'sq ft'),
        sq_ft_pitchctrl = U(None, 'sq ft'),
        sq_ft_strakes = U(None, 'sq ft'),
        sq_ft_ailerons = U(None, 'sq ft'),
        sq_ft_leadingflaps = U(None, 'sq ft'),
        sq_ft_trailingflaps = U(None, 'sq ft'),
        sq_ft_vertsurf = U(None, 'sq ft'),
        taper_ratio_wing = U(None, ''),
        taper_ratio_pitchctrl = U(None, ''),
        taper_ratio_strakes = U(None, ''),
        taper_ratio_ailerons = U(None, ''),
        taper_ratio_leadingflaps = U(None, ''),
        taper_ratio_trailingflaps = U(None, ''),
        taper_ratio_vertsurf = U(None, ''),
        aspect_ratio_wing = U(None, ''),
        aspect_ratio_pitchctrl = U(None, ''),
        aspect_ratio_strakes = U(None, ''),
        aspect_ratio_ailerons = U(None, ''),
        aspect_ratio_leadingflaps = U(None, ''),
        aspect_ratio_trailingflaps = U(None, ''),
        aspect_ratio_vertsurf = U(None, ''),
        tilt_deg_vertsurf = U(None, '°')):
            self.sweep_deg_wing = sweep_deg_wing
            self.sweep_deg_pitchctrl = sweep_deg_pitchctrl
            self.sweep_deg_strakes = sweep_deg_strakes
            self.sweep_deg_ailerons = sweep_deg_ailerons
            self.sweep_deg_leadingflaps = sweep_deg_leadingflaps
            self.sweep_deg_trailingflaps = sweep_deg_trailingflaps
            self.sweep_deg_vertsurf = sweep_deg_vertsurf
            self.sq_ft_wing = sq_ft_wing
            self.sq_ft_pitchctrl = sq_ft_pitchctrl
            self.sq_ft_strakes = sq_ft_strakes
            self.sq_ft_ailerons = sq_ft_ailerons
            self.sq_ft_leadingflaps = sq_ft_leadingflaps
            self.sq_ft_trailingflaps = sq_ft_trailingflaps
            self.sq_ft_vertsurf = sq_ft_vertsurf
            self.taper_ratio_wing = taper_ratio_wing
            self.taper_ratio_pitchctrl = taper_ratio_pitchctrl
            self.taper_ratio_strakes = taper_ratio_strakes
            self.taper_ratio_ailerons = taper_ratio_ailerons
            self.taper_ratio_leadingflaps = taper_ratio_leadingflaps
            self.taper_ratio_trailingflaps = taper_ratio_trailingflaps
            self.taper_ratio_vertsurf = taper_ratio_vertsurf
            self.aspect_ratio_wing = aspect_ratio_wing
            self.aspect_ratio_pitchctrl = aspect_ratio_pitchctrl
            self.aspect_ratio_strakes = aspect_ratio_strakes
            self.aspect_ratio_ailerons = aspect_ratio_ailerons
            self.aspect_ratio_leadingflaps = aspect_ratio_leadingflaps
            self.aspect_ratio_trailingflaps = aspect_ratio_trailingflaps
            self.aspect_ratio_vertsurf = aspect_ratio_vertsurf
            self.tilt_deg_vertsurf = tilt_deg_vertsurf

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, U(try_to_float(value), vars(self)[new_key].unit))

    def push_values_to_dict(self):
        dictionary = {}
        for key, value in vars(self).items():
            split_list = [k.capitalize() for k in key.split('_')]
            key1 = ''.join(split_list[:2])
            key2 = split_list[-1]
            if key1 not in dictionary:
                dictionary[key1] = {}
                dictionary[key1][key2] = try_to_float(value.value)
            else:
                dictionary[key1][key2] = try_to_float(value.value)
        return dictionary

    def push_units_to_dict(self):
        dictionary = {}
        for key, value in vars(self).items():
            split_list = [k.capitalize() for k in key.split('_')]
            key1 = ''.join(split_list[:2])
            key2 = split_list[-1]
            if key1 not in dictionary:
                dictionary[key1] = {}
                dictionary[key1][key2] = value.unit
            else:
                dictionary[key1][key2] = value.unit
        return dictionary

