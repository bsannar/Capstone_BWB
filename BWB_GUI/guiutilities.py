from PySide6.QtWidgets import QCheckBox

def clearLayout(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget():
      child.widget().deleteLater()

def get_key_structure(dictionary):
  keys = []
  for key, d in dictionary.items():
      if isinstance(d, dict):
          keys.append({key: get_key_structure(d)})
      else:
          keys.append(key)
  return keys

def flatten_dict(dictionary):
    flattened_dict = {}
    keys = get_key_structure(dictionary)
    for key in keys:
        if isinstance(key, dict):
            key1, keys2 = list(key.items())[0]
            for key2 in keys2:
                flattened_dict[key1+key2] = dictionary[key1][key2]
        else:
            flattened_dict[key] = dictionary[key]
    return flattened_dict

def float_eq(float_1, float_2):
    return round(float_1, 6) == round(float_2, 6)

def try_to_float(str):
    try:
        return float(str)
    except:
        return 0

def get_checked_checkboxes_from_layout(layout):
    list = []
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if isinstance(widget, QCheckBox):
            if widget.isChecked():
                list.append(widget.text())
    return list
