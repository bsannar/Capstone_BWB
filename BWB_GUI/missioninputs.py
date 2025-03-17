from textprocessingutilities import *
from guiutilities import flatten_dict
from internalstorageinterface import InternalStorageInterface
from units import U

class MissionInputs(InternalStorageInterface):
    def __init__(self,
        alt_takeoff = U(0, 'ft'),
        alt_accel = U(None, 'ft'),
        alt_climb1 = U(None, 'ft'),
        alt_cruise1 = U(None, 'ft'),
        alt_patrol1 = U(None, 'ft'),
        alt_service1 = U(None, 'ft'),
        alt_patrol2 = U(None, 'ft'),
        alt_service2 = U(None, 'ft'),
        alt_patrol3 = U(None, 'ft'),
        alt_service3 = U(None, 'ft'),
        alt_climb2 = U(None, 'ft'),
        alt_cruise2 = U(None, 'ft'),
        alt_loiter = U(None, 'ft'),
        alt_landing = U(0,'ft'),
        mach_takeoff = U(None, 'mach'),
        mach_accel = U(None, 'mach'),
        mach_climb1 = U(None, 'mach'),
        mach_cruise1 = U(None, 'mach'),
        mach_patrol1 = U(None, 'mach'),
        mach_service1 = U(None, 'mach'),
        mach_patrol2 = U(None, 'mach'),
        mach_service2 = U(None, 'mach'),
        mach_patrol3 = U(None, 'mach'),
        mach_service3 = U(None, 'mach'),
        mach_climb2 = U(None, 'mach'),
        mach_cruise2 = U(None, 'mach'),
        mach_loiter = U(None, 'mach'),
        dist_takeoff = U(None, 'ft'),
        dist_accel = U(None, 'nm'),
        dist_climb1 = U(None, 'nm'),
        dist_cruise1 = U(None, 'nm'),
        dist_patrol1 = U(None, 'nm'),
        dist_service1 = U(None, 'nm'),
        dist_patrol2 = U(None, 'nm'),
        dist_service2 = U(None, 'nm'),
        dist_patrol3 = U(None, 'nm'),
        dist_service3 = U(None, 'nm'),
        dist_climb2 = U(None, 'nm'),
        dist_cruise2 = U(None, 'nm'),
        dist_loiter = U(None, 'nm'),
        time_takeoff = U(None, 'min'),
        time_accel = U(None, 'min'),
        time_climb1 = U(None, 'min'),
        time_cruise1 = U(None, 'min'),
        time_patrol1 = U(None, 'min'),
        time_service1 = U(None, 'min'),
        time_patrol2 = U(None, 'min'),
        time_service2 = U(None, 'min'),
        time_patrol3 = U(None, 'min'),
        time_service3 = U(None, 'min'),
        time_climb2 = U(None, 'min'),
        time_cruise2 = U(None, 'min'),
        time_loiter = U(None, 'min'),
        payload_takeoff = U(None, 'lbs'),
        payload_accel = U(None, 'lbs'),
        payload_climb1 = U(None, 'lbs'),
        payload_cruise1 = U(None, 'lbs'),
        payload_patrol1 = U(None, 'lbs'),
        payload_service1 = U(None, 'lbs'),
        payload_patrol2 = U(None, 'lbs'),
        payload_service2 = U(None, 'lbs'),
        payload_patrol3 = U(None, 'lbs'),
        payload_service3 = U(None, 'lbs'),
        payload_climb2 = U(None, 'lbs'),
        payload_cruise2 = U(None, 'lbs'),
        payload_loiter = U(None, 'lbs'),
        exp_payload = U(None, 'lbs'),
        perm_payload = U(None, 'lbs')):
            self.alt_takeoff = alt_takeoff
            self.alt_accel = alt_accel
            self.alt_climb1 = alt_climb1
            self.alt_cruise1 = alt_cruise1
            self.alt_patrol1 = alt_patrol1
            self.alt_service1 = alt_service1
            self.alt_patrol2 = alt_patrol2
            self.alt_service2 = alt_service2
            self.alt_patrol3 = alt_patrol3
            self.alt_service3 = alt_service3
            self.alt_climb2 = alt_climb2
            self.alt_cruise2 = alt_cruise2
            self.alt_loiter = alt_loiter
            self.alt_landing = alt_landing
            self.mach_takeoff = mach_takeoff
            self.mach_accel = mach_accel
            self.mach_climb1 = mach_climb1
            self.mach_cruise1 = mach_cruise1
            self.mach_patrol1 = mach_patrol1
            self.mach_service1 = mach_service1
            self.mach_patrol2 = mach_patrol2
            self.mach_service2 = mach_service2
            self.mach_patrol3 = mach_patrol3
            self.mach_service3 = mach_service3
            self.mach_climb2 = mach_climb2
            self.mach_cruise2 = mach_cruise2
            self.mach_loiter = mach_loiter
            self.dist_takeoff = dist_takeoff
            self.dist_accel = dist_accel
            self.dist_climb1 = dist_climb1
            self.dist_cruise1 = dist_cruise1
            self.dist_patrol1 = dist_patrol1
            self.dist_service1 = dist_service1
            self.dist_patrol2 = dist_patrol2
            self.dist_service2 = dist_service2
            self.dist_patrol3 = dist_patrol3
            self.dist_service3 = dist_service3
            self.dist_climb2 = dist_climb2
            self.dist_cruise2 = dist_cruise2
            self.dist_loiter = dist_loiter
            self.time_takeoff = time_takeoff
            self.time_accel = time_accel
            self.time_climb1 = time_climb1
            self.time_cruise1 = time_cruise1
            self.time_patrol1 = time_patrol1
            self.time_service1 = time_service1
            self.time_patrol2 = time_patrol2
            self.time_service2 = time_service2
            self.time_patrol3 = time_patrol3
            self.time_service3 = time_service3
            self.time_climb2 = time_climb2
            self.time_cruise2 = time_cruise2
            self.time_loiter = time_loiter
            self.payload_takeoff = payload_takeoff
            self.payload_accel = payload_accel
            self.payload_climb1 = payload_climb1
            self.payload_cruise1 = payload_cruise1
            self.payload_patrol1 = payload_patrol1
            self.payload_service1 = payload_service1
            self.payload_patrol2 = payload_patrol2
            self.payload_service2 = payload_service2
            self.payload_patrol3 = payload_patrol3
            self.payload_service3 = payload_service3
            self.payload_climb2 = payload_climb2
            self.payload_cruise2 = payload_cruise2
            self.payload_loiter = payload_loiter
            self.exp_payload = exp_payload
            self.perm_payload = perm_payload

    def pull_from_dict(self, dictionary: dict):
        flattened_dict = flatten_dict(dictionary)
        for key, value in flattened_dict.items():
            new_key = convert_from_camel_casing_to_underscores(key)
            setattr(self, new_key, U(value, vars(self)[new_key].unit))

    def push_to_dict(self):
        dictionary = {}
        for key, value in vars(self).items():
            key1, key2 = [k.capitalize() for k in key.split('_')]
            if key1 not in dictionary:
                if key2 == "Payload":
                    dictionary[key1+key2] = value.value
                else:
                    dictionary[key1] = {}
                    dictionary[key1][key2] = value.value
            else:
                dictionary[key1][key2] = value.value
        return dictionary
