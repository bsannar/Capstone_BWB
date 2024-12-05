# This Python file uses the following encoding: utf-8
import sys
import os
import signal
from functions import Functions

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QProcess

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
        self.process = QProcess()
        self.functions = Functions(self.ui, self.process)
        self.xl = self.functions.xl
        self.wb = self.functions.wb
        self.hasPlotted = True

    def closeEvent(self, *args, **kwargs):
        if self.process.state == "ProcessState.Running":
            os.kill(self.process.processId(), signal.SIGTERM)
        super().closeEvent(*args, **kwargs)
        self.wb.close()
        self.xl.quit()

    def resizeEvent(self, event):
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
