from PySide6.QtWidgets import QTableWidgetItem

def calculate_sensitivity_from_jet(ui, bwb, mainSheet, cell):
    centerValue = float(bwb.sqFtWing)
    stepSize = centerValue * 0.1
    mainSheet[cell].value = centerValue + 0.5*stepSize
    forward = calculate_max_range(mainSheet)
    mainSheet[cell].value = centerValue - 0.5*stepSize
    backward = calculate_max_range(mainSheet)
    drange_dsqftwing = (forward - backward) / stepSize
    rowPosition = ui.tblSensitivities.rowCount()
    colPosition = ui.tblSensitivities.columnCount()
    ui.tblSensitivities.insertColumn(colPosition)
    ui.tblSensitivities.setHorizontalHeaderLabels(["Range"])
    ui.tblSensitivities.insertRow(rowPosition)
    ui.tblSensitivities.setVerticalHeaderLabels(["Wing Square Footage"])
    ui.tblSensitivities.setItem(rowPosition, 0, QTableWidgetItem(str(drange_dsqftwing)))

def calculate_max_range(mainSheet):
    mainSheet["O17"].value = 0
    for nautical_miles in range(1, 10000):
        set_payload_drop_distance(mainSheet, nautical_miles*50)
        if mainSheet["X40"].value > mainSheet["O18"].value:
            return (nautical_miles-1)*100

def set_payload_drop_distance(mainSheet, payloadDropDistance):
    mainSheet["N38"].value = payloadDropDistance - mainSheet["M38"].value - mainSheet["P38"].value - mainSheet["L38"].value
