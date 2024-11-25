import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from tixi3 import tixi3wrapper
from tigl3.configuration import CCPACSConfiguration
from OpenGL.GL import *

class TiGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config = None
        self.shape = None
        cpacs_file = "Assets/theAircraft.xml"
        self.load_cpacs_file(cpacs_file)

    def load_cpacs_file(self, file_path):
        """Load CPACS file using TiGL."""
        tixi = tixi3wrapper.Tixi3()
        tixi.open(file_path)
        self.config = CCPACSConfiguration(tixi._handle.value)
        self.shape = self.config.get_shape_cache().get_shape(str(tixi._handle.value))

    def initializeGL(self):
        """Initialize OpenGL settings."""
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, width, height):
        """Handle window resizing."""
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = width / height if height > 0 else 1
        glOrtho(-1 * aspect_ratio, 1 * aspect_ratio, -1, 1, -10, 10)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        """Render the TiGL geometry."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        if self.shape:
            self.render_tigl_shape()

    def render_tigl_shape(self):
        """Render the TiGL shape."""
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_TRIANGLES)
        print(dir(self.shape))
        for face in self.shape.get_faces():
            for vertex in face.get_vertices():
                glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()
