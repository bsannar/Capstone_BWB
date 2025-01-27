# This Python file uses the following encoding: utf-8
import sys
import os
import signal
from functions import Functions
from jetinterface import JetInterface
from textprocessingutilities import split_camel_casing

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
        self.generate_ui_mission_dict()
        self.generate_ui_geometry_dict()
        self.setWindowIcon(QPixmap("App_Icon.png"))
        self.process = QProcess()
        self.interface = JetInterface(self.ui, self.ui_mission_dict, self.ui_geometry_dict)
        self.functions = Functions(self.ui, self.process, self.interface)
        self.hasPlotted = True

    def closeEvent(self, *args, **kwargs):
        if self.process.state == "ProcessState.Running":
            os.kill(self.process.processId(), signal.SIGTERM)
        super().closeEvent(*args, **kwargs)
        self.interface.close_interface()

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def generate_ui_mission_dict(self):
        dict = {}
        widgets = [self.ui.glDenseMissionParameters.itemAt(i).widget() for i in range(self.ui.glDenseMissionParameters.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = split_camel_casing(name)[-1]
            key2 = ''.join(split_camel_casing(name)[1:-1])
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = w
        dict["ExpPayload"] = self.ui.txtExpendablePayload
        dict["PermPayload"] = self.ui.txtPermanentPayload
        self.ui_mission_dict = dict

    def generate_ui_geometry_dict(self):
        dict = {}
        widgets = [self.ui.glBwbGeometry.itemAt(i).widget() for i in range(self.ui.glBwbGeometry.count())]
        text_widgets = [w for w in widgets if w.objectName().startswith("txt")]
        for i, w in enumerate(text_widgets):
            name = w.objectName()
            key1 = ''.join(split_camel_casing(name)[2:])
            key2 = split_camel_casing(name)[1]
            if key1 not in dict:
                dict[key1] = {}
            dict[key1][key2] = w
        #dict["TiltDeg"] = self.ui.txtVertsurfTiltDeg
        self.ui_geometry_dict = dict

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
