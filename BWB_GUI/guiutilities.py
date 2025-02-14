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
