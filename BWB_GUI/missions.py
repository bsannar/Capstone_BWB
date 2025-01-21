from PySide6.QtWidgets import QLabel, QLineEdit
import re
import csv
import os

def copy_mission_to_ui(mission_dict, ui_dict):
    for key1, dict in ui_dict.items():
        if key1 == "ExpPayload" or key1 == "PermPayload":
            ui_dict[key1].setText(str(mission_dict[key1]))
        else:
            for key2, val in dict.items():
                ui_dict[key1][key2].setText(str(mission_dict[key1][key2]))

def populate_ui_from_csv(ui, name):
    mission_dict = load_mission_from_csv(f"Assets/Missions/{name}.csv")
    ui_dict = generate_mission_ui_dictionary(ui)
    copy_mission_to_ui(mission_dict, ui_dict)

def setup_airdrop_mission(ui):
    mission_dict = load_mission_from_csv("Assets/Airdrop.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_drop_distance(text, ui))
    txtDistanceToDropSite.setText(str(mission_dict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_payload_weight(text, ui))
    txtPayloadWeight.setText(str(mission_dict["Payload"]["Service2"]))

    # ui.glMissionParameters.addWidget(QLabel("Drop altitude:"), 2, 0)
    # txtDropAlt = QLineEdit()
    # ui.glMissionParameters.addWidget(txtDropAlt, 2, 1)
    # txtDropAlt.textChanged.connect(lambda text: set_drop_altitude(text, ui))

    ui_dict = generate_mission_ui_dictionary(ui)
    copy_mission_to_ui(mission_dict, ui_dict)

def setup_tanker_mission(ui):
    mission_dict = load_mission_from_csv("Assets/Tanker.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to F35s:"), 0, 0)
    txtDistanceToF35s = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToF35s, 0, 1)
    txtDistanceToF35s.textChanged.connect(lambda text: set_f35s_distance(text, ui))
    txtDistanceToF35s.setText(str(mission_dict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("F35s to refuel:"), 1, 0)
    txtF35sToRefuel = QLineEdit()
    ui.glMissionParameters.addWidget(txtF35sToRefuel, 1, 1)
    txtF35sToRefuel.textChanged.connect(lambda text: set_f35s_to_refuel(text, ui))

    ui_dict = generate_mission_ui_dictionary(ui)
    copy_mission_to_ui(mission_dict, ui_dict)

def setup_cargo_carry_mission(ui):
    mission_dict = load_mission_from_csv("Assets/Cargo Carry.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_carry_distance(text, ui))
    txtDistanceToDropSite.setText(str(mission_dict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_carry_weight(text, ui))
    txtPayloadWeight.setText(mission_dict["PermPayload"])

    ui_dict = generate_mission_ui_dictionary(ui)
    copy_mission_to_ui(mission_dict, ui_dict)

def set_drop_distance(text, ui):
    ui.txtCruise1Dist.setText(text)
    ui.txtCruise2Dist.setText(text)

def set_carry_distance(text, ui):
    ui.txtCruise1Dist.setText(text)

def set_carry_weight(text, ui):
    ui.txtPermanentPayload.setText(text)

def set_f35s_distance(text, ui):
    ui.txtCruise1Dist.setText(text)
    ui.txtCruise2Dist.setText(text)

def set_f35s_to_refuel(text, ui):
    try:
        num_f35s = int(text)
    except:
        num_f35s = 0
    f35_max_fuel = 18000 #lbs
    refuel_capacity = 0.8
    fuel_weight = num_f35s*f35_max_fuel*refuel_capacity
    ui.txtService2Payload.setText(str(fuel_weight))
    ui.txtExpendablePayload.setText(str(fuel_weight))

def set_payload_weight(text, ui):
    ui.txtService2Payload.setText(text)
    ui.txtExpendablePayload.setText(text)

def set_drop_Alt(text, ui):
    ui.txtPatrol1Alt.setText(text)
    ui.txtService1Alt.setText(text)
    ui.txtPatrol2Alt.setText(text)
    ui.txtService2Alt.setText(text)
    ui.txtPatrol3Alt.setText(text)
    ui.txtService3Alt.setText(text)

def get_last_word(text):
    return re.findall("[A-Z][a-z]*", text)[-1]

def strip_last_word_and_prefix(text):
    last_word = get_last_word(text)
    prefix = re.findall("[a-z]*", text)[0]
    return re.sub(f"{last_word}|{prefix}", '', text)

def generate_mission_ui_dictionary(ui):
    dict = {}
    widgets = [ui.glDenseMissionParameters.itemAt(i).widget() for i in range(ui.glDenseMissionParameters.count())]
    text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
    for w in text_widgets:
        key = get_last_word(w.objectName())
        if key not in dict:
            dict[key] = {}
    for w in text_widgets:
        name = w.objectName()
        dict[get_last_word(name)][strip_last_word_and_prefix(name)] = w
    dict["ExpPayload"] = ui.txtExpendablePayload
    dict["PermPayload"] = ui.txtPermanentPayload
    return dict

def load_mission_from_csv(file):
    dict = {}
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(csvreader):
            if i == 0:
                keys = row[1:]
            else:
                for j, val in enumerate(row):
                    if j == 0:
                        key = val
                        if key != "ExpPayload" and key != "PermPayload":
                            dict[key] = {}
                    else:

                        if key == "ExpPayload" or key == "PermPayload":
                            dict[key] = val
                            break
                        else:
                            dict[key][keys[j-1]] = val
    return dict

def generate_jet_dict(ui):
    cell_dict = {"Alt": "33", "Mach": "35", "Dist": "38", "Time": "39", "Payload": "41",
        "TO": "K", "Accel": "L", "Climb1": "M", "Cruise1": "N", "Patrol1": "O", "Service1": "P", "Patrol2": "Q", "Service2": "R", "Patrol3": "S", "Service3": "T", "Climb2": "U", "Cruise2": "V", "Loiter": "W", "Landing": "X"}
    dict = {}
    widgets = [ui.glDenseMissionParameters.itemAt(i).widget() for i in range(ui.glDenseMissionParameters.count())]
    text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
    for w in text_widgets:
        key = get_last_word(w.objectName())
        if key not in dict:
            dict[key] = {}
    for i, w in enumerate(text_widgets):
        name = w.objectName()
        key1 = get_last_word(name)
        key2 = strip_last_word_and_prefix(name)
        dict[key1][key2] = cell_dict[key2]+cell_dict[key1]
    dict["ExpPayload"] = "O17"
    dict["PermPayload"] = "O16"
    print(dict)
    return dict

def populate_jet(ui, main_sheet):
    ui_dict = generate_mission_ui_dictionary(ui)
    jet_dict = generate_jet_dict(ui)
    for key1, dict in ui_dict.items():
        if key1 == "ExpPayload" or key1 == "PermPayload":
            main_sheet[jet_dict[key1]].value = ui_dict[key1].text()
        else:
            for key2, val in dict.items():
                main_sheet[jet_dict[key1][key2]].value = ui_dict[key1][key2].text()

def create_mission_csv(ui, name):
    ui_dict = generate_mission_ui_dictionary(ui)
    if not os.path.exists("Assets/Missions/"):
        os.makedirs("Assets/Missions/")
    with open(f"Assets/Missions/{name}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        header = ['']
        header2 = [[key2 for key2, val in dict.items()] for key1, dict in ui_dict.items() if key1 != "ExpPayload" and key1 != "PermPayload"][0]
        header.extend(header2)
        row_dict = {key: i for i, key in enumerate(header)}
        writer.writerow(header)
        for key1, dict in ui_dict.items():
            if key1 == "ExpPayload" or key1 == "PermPayload":
                writer.writerow([key1, ui_dict[key1].text()])
            else:
                row = header
                row[0] = key1
                for key2, val in dict.items():
                    row[row_dict[key2]] = (ui_dict[key1][key2].text())
                writer.writerow(row)


