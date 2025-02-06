from PySide6.QtWidgets import QLabel, QLineEdit
from datamanager import DataManager
from csvinterface import CsvInterface

def setup_airdrop_mission(gui_manager):
    interface = CsvInterface("Assets/Airdrop.csv")
    data_manager = DataManager(interface, gui_manager)
    mission_dict = interface.pull_from_storage()

    gui_manager.ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_drop_distance(text, gui_manager.ui))
    txtDistanceToDropSite.setText(str(mission_dict["Dist"]["Cruise1"]))

    gui_manager.ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_payload_weight(text, gui_manager.ui))
    txtPayloadWeight.setText(str(mission_dict["Payload"]["Service2"]))

    # ui.glMissionParameters.addWidget(QLabel("Drop altitude:"), 2, 0)
    # txtDropAlt = QLineEdit()
    # ui.glMissionParameters.addWidget(txtDropAlt, 2, 1)
    # txtDropAlt.textChanged.connect(lambda text: set_drop_altitude(text, ui))

    data_manager.transfer_mission_inputs()

def setup_tanker_mission(gui_manager):
    interface = CsvInterface("Assets/Tanker.csv")
    data_manager = DataManager(interface, gui_manager)
    mission_dict = interface.pull_from_storage()

    gui_manager.ui.glMissionParameters.addWidget(QLabel("Distance to F35s:"), 0, 0)
    txtDistanceToF35s = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtDistanceToF35s, 0, 1)
    txtDistanceToF35s.textChanged.connect(lambda text: set_f35s_distance(text, gui_manager.ui))
    txtDistanceToF35s.setText(str(mission_dict["Dist"]["Cruise1"]))

    gui_manager.ui.glMissionParameters.addWidget(QLabel("F35s to refuel:"), 1, 0)
    txtF35sToRefuel = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtF35sToRefuel, 1, 1)
    txtF35sToRefuel.textChanged.connect(lambda text: set_f35s_to_refuel(text, gui_manager.ui))

    data_manager.transfer_mission_inputs()

def setup_cargo_carry_mission(gui_manager):
    interface = CsvInterface("Assets/Cargo Carry.csv")
    data_manager = DataManager(interface, gui_manager)
    mission_dict = interface.pull_from_storage()

    gui_manager.ui.glMissionParameters.addWidget(QLabel("Distance to drop site (nm):"), 0, 0)
    txtDistanceToDropSite = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtDistanceToDropSite, 0, 1)
    txtDistanceToDropSite.textChanged.connect(lambda text: set_carry_distance(text, gui_manager.ui))
    txtDistanceToDropSite.setText(str(mission_dict["Dist"]["Cruise1"]))

    gui_manager.ui.glMissionParameters.addWidget(QLabel("Payload weight (lb):"), 1, 0)
    txtPayloadWeight = QLineEdit()
    gui_manager.ui.glMissionParameters.addWidget(txtPayloadWeight, 1, 1)
    txtPayloadWeight.textChanged.connect(lambda text: set_carry_weight(text, gui_manager.ui))
    txtPayloadWeight.setText(mission_dict["PermPayload"])

    data_manager.transfer_mission_inputs()

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


