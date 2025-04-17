# This Python file uses the following encoding: utf-8
import sys
import os
import signal
from guimanager import GuiManager

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

if hasattr(sys, '_MEIPASS'):
    # Set the path to the bundled platform plugins
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = sys._MEIPASS
    if os.name == 'posix':
        os.environ['QT_QPA_PLATFORM'] = 'xcb'

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QPixmap("App_Icon.png"))
        self.gui_manager = GuiManager(self.ui, self.repaint)

    def closeEvent(self, *args, **kwargs):
        if self.gui_manager.bwb_process.state == "ProcessState.Running":
            os.kill(self.gui_manager.bwb_process.processId(), signal.SIGTERM)
        if self.gui_manager.taw_process.state == "ProcessState.Running":
            os.kill(self.gui_manager.taw_process.processId(), signal.SIGTERM)
        self.gui_manager.jet_bwb_interface.close_interface()
        self.gui_manager.jet_taw_interface.close_interface()
        super().closeEvent(*args, **kwargs)

    def resizeEvent(self, event):
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
