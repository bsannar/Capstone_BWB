from PySide6.QtWidgets import QLabel, QLineEdit
import re
import csv

def setup_airdrop_mission(ui):
    missionDict = load_mission_from_csv("Assets/Airdrop.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_drop_distance(text, ui))
    txtDistanceToDropSite.setText(str(missionDict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_payload_weight(text, ui))
    txtPayloadWeight.setText(str(missionDict["Payload"]["Service2"]))

    # ui.glMissionParameters.addWidget(QLabel("Drop altitude:"), 2, 0)
    # txtDropAlt = QLineEdit()
    # ui.glMissionParameters.addWidget(txtDropAlt, 2, 1)
    # txtDropAlt.textChanged.connect(lambda text: set_drop_altitude(text, ui))

    ui_dict = generate_mission_ui_dictionary(ui)
    for key1, dict in ui_dict.items():
        for key2, val in dict.items():
            ui_dict[key1][key2].setText(str(missionDict[key1][key2]))

    ui.txtPermanentPayload.setText("0")
    ui.txtExpendablePayload.setText(ui_dict["Payload"]["Service2"].text())

def setup_tanker_mission(ui):
    missionDict = load_mission_from_csv("Assets/Tanker.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to F35s:"), 0, 0)
    txtDistanceToF35s = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToF35s, 0, 1)
    txtDistanceToF35s.textChanged.connect(lambda text: set_f35s_distance(text, ui))
    txtDistanceToF35s.setText(str(missionDict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("F35s to refuel:"), 1, 0)
    txtF35sToRefuel = QLineEdit()
    ui.glMissionParameters.addWidget(txtF35sToRefuel, 1, 1)
    txtF35sToRefuel.textChanged.connect(lambda text: set_f35s_to_refuel(text, ui))

    ui_dict = generate_mission_ui_dictionary(ui)
    for key1, dict in ui_dict.items():
        for key2, val in dict.items():
            ui_dict[key1][key2].setText(str(missionDict[key1][key2]))

    ui.txtPermanentPayload.setText("0")
    ui.txtExpendablePayload.setText(ui_dict["Payload"]["Service2"].text())

def setup_cargo_carry_mission(ui):
    missionDict = load_mission_from_csv("Assets/Cargo Carry.csv")

    ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_carry_distance(text, ui))
    txtDistanceToDropSite.setText(str(missionDict["Dist"]["Cruise1"]))

    ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_carry_weight(text, ui))
    txtPayloadWeight.setText("164900")

    ui_dict = generate_mission_ui_dictionary(ui)
    for key1, dict in ui_dict.items():
        for key2, val in dict.items():
            ui_dict[key1][key2].setText(str(missionDict[key1][key2]))

    ui.txtPermanentPayload.setText("164900")
    ui.txtExpendablePayload.setText("0")

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
                        dict[key] = {}
                    else:
                        dict[key][keys[j-1]] = val
    return dict
