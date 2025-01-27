import re

def convert_from_camel_casing(string):
    output = ""
    for s in string:
        if s.isupper():
            output += " " + s
        else:
            output += s
    return str.upper(output[0]) + output[1:]

def convert_to_camel_casing(string):
    return str.lower(string[0]) + string[1:].replace(" ", "")

def split_camel_casing(string):
    output = ""
    for s in string:
        if s.isupper():
            output += " " + s
        else:
            output += s
    return output.split(" ")
