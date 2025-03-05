from PySide6.QtWidgets import QDialog, QProgressBar, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
import numpy as np

class LoadingBar:
    class Range(QDialog):
        def __init__(self, start, stop=None, step=None, message='Loading...'):
            if type(start) == int:
                start = (start,)
            if type(stop) == int:
                stop = (stop,)
            if type(step) == int:
                step = (step,)

            if stop == None:
                stop = start
                start = tuple(0 for i in range(len(start)))
            if step == None:
                step = tuple(1 for i in range(len(start)))

            self.iterations = tuple((stop - start - 1) // step + 1 for start, stop, step in zip(start, stop, step))
            self.step = step
            self.start = start
            self.total_iterations = np.prod(self.iterations)

            super().__init__()
            self.setWindowTitle(message)

            layout = QVBoxLayout()
            self.bar = QProgressBar(self)
            self.bar.setRange(0, self.total_iterations)
            self.bar.setValue(0)
            self.bar.setAlignment(Qt.AlignCenter)

            self.bar.setStyleSheet("""
                QProgressBar {
                    text-align: center;
                    border-radius: 10px; /* Rounded corners */
                }
                QProgressBar::chunk {
                    background-color: #3b7ddd; /* Progress color */
                    border-radius: 10px; /* Smooth edges */
                }
            """)

            layout.addWidget(self.bar)
            self.setLayout(layout)
            self.show()

        def get_indices(self):
            indices = []
            index = self.bar.value()-1
            for i in range(len(self.iterations)-1):
                indices.append(index // np.prod(self.iterations[i+1:]) % np.prod(self.iterations[i:]))
            indices.append(index % self.iterations[-1])
            values = tuple(i*step + start for i, step, start in zip(indices, self.step, self.start))
            if len(values) == 1:
                return values[0]
            return values

        def __iter__(self):
            """Returns the iterator itself."""
            return self

        def __next__(self):
            """Advances the progress bar at each iteration."""
            if self.bar.value() >= self.total_iterations:
                self.close()
                raise StopIteration

            self.bar.setValue(self.bar.value() + 1)
            QApplication.processEvents()

            return self.get_indices()

    class List(QDialog):
        def __init__(self, list, message='Loading...'):

            self.list = list
            self.iterations = len(list)

            super().__init__()
            self.setWindowTitle(message)

            layout = QVBoxLayout()
            self.bar = QProgressBar(self)
            self.bar.setRange(0, self.iterations)
            self.bar.setValue(0)
            self.bar.setAlignment(Qt.AlignCenter)

            self.bar.setStyleSheet("""
                QProgressBar {
                    text-align: center;
                    border-radius: 10px; /* Rounded corners */
                }
                QProgressBar::chunk {
                    background-color: #3b7ddd; /* Progress color */
                    border-radius: 10px; /* Smooth edges */
                }
            """)

            layout.addWidget(self.bar)
            self.setLayout(layout)
            self.show()

        def __iter__(self):
            """Returns the iterator itself."""
            return self

        def __next__(self):
            """Advances the progress bar at each iteration."""
            if self.bar.value() >= self.iterations:
                self.close()
                raise StopIteration

            self.bar.setValue(self.bar.value() + 1)
            QApplication.processEvents()

            return self.list[self.bar.value() - 1]
