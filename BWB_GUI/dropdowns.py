from PySide6.QtWidgets import QMenu, QToolButton
from PySide6.QtGui import QAction, QActionGroup

def setup_dropdown(toolButton, dropdownList, multi_select = False):
    toolMenu = QMenu(toolButton)
    actionGroup = QActionGroup(toolMenu)
    actionGroup.setExclusive(not multi_select)
    for item in dropdownList:
        action = QAction(item, toolButton)
        action.setCheckable(True)
        toolMenu.addAction(action)
        actionGroup.addAction(action)
    toolButton.setMenu(toolMenu)
    toolButton.setPopupMode(QToolButton.InstantPopup)
