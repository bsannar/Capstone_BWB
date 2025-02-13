import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout

class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent):
        fig = Figure(layout='tight')
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        toolbar = NavigationToolbar(self)
        layout = QVBoxLayout(parent)
        layout.addWidget(toolbar)
        layout.addWidget(self)
        parent.setLayout(layout)

