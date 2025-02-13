import re

def convert_from_camel_casing_to_spaces(string):
    output = ""
    for s in string:
        if s.isupper() and s != string[0]:
            output += " " + s
        else:
            output += s
    return str.upper(output[0]) + output[1:]

def convert_from_camel_casing_to_underscores(string):
    output = ""
    for i, s in enumerate(string):
        if s.isupper() and i != 0:
            output += "_" + str.lower(s)
        else:
            output += str.lower(s)
    return output

def convert_to_camel_casing_from_spaces(string):
    return str.lower(string[0]) + string[1:].replace(" ", "")

def convert_to_camel_casing_from_underscores(string):
    return str.lower(string.replace("_", ""))

def convert_to_underscores_from_spaces(string):
    return string.replace(" ", "_")

def convert_to_spaces_from_underscores(string):
    return string.replace("_", " ")

def split_camel_casing(string):
    output = ""
    for s in string:
        if s.isupper():
            output += " " + s
        else:
            output += s
    return output.split(" ")

def format_number(number_string):
    return f"{float(number_string):.4g}"

def to_float(number_string):
    try:
        return float(number_string)
    except ValueError:
        return 0.0
