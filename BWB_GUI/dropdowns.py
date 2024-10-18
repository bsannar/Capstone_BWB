from PySide6.QtWidgets import QMenu, QToolButton

def setup_dropdown(toolButton, dropdownList):
    toolMenu = QMenu(toolButton)
    for item in dropdownList:
        action = toolMenu.addAction(item)
        action.setCheckable(True)
    toolButton.setMenu(toolMenu)
    toolButton.setPopupMode(QToolButton.InstantPopup)
