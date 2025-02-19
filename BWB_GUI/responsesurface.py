import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator
from datamanager import DataManager

class ResponseSurface:
    def __init__(self, canvas, x_min, x_max, x_steps, y_min, y_max, y_steps, x_name, y_name, r_name, loaded_aircraft, tool_interface):
        self.canvas = canvas
        self.x_min = float(x_min)
        self.x_max = float(x_max)
        self.x_steps = int(x_steps)
        self.y_min = float(y_min)
        self.y_max = float(y_max)
        self.y_steps = int(y_steps)
        self.x_name = x_name
        self.y_name = y_name
        self.r_name = r_name
        self.loaded_aircraft = loaded_aircraft
        self.data_manager = DataManager(tool_interface, self.loaded_aircraft)
        
        self.initialize_grid()
        self.interpolate_response()
        self.create_plot()
    
    def compute_response(self):
        self.canvas.ax.cla()
        vx, vy = np.meshgrid(self.x, self.y, indexing='ij')
        response = np.zeros((self.x_steps, self.y_steps))
        points = []
        for i in range(self.x_steps):
            for j in range(self.y_steps):
                print(i, j)
                x_name = self.x_name.replace(" ", "_")
                y_name = self.y_name.replace(" ", "_")
                geometry_dict = {x_name: vx[i, j], y_name: vy[i, j]}
                self.loaded_aircraft.geometry.pull_from_dict(geometry_dict)
                self.data_manager.transfer_max_range()
                response[i, j] = self.loaded_aircraft.mission_outputs.max_range
                points.append((vx[i, j], vy[i, j], response[i, j]))
        self.canvas.ax.scatter(points[0], points[1], points[2])
        return response

    def initialize_grid(self):
        self.x = np.linspace(self.x_min, self.x_max, self.x_steps)
        self.y = np.linspace(self.y_min, self.y_max, self.y_steps)
        self.response = self.compute_response()
        self.grid_old = (self.x, self.y)
        
        self.x_new = np.linspace(self.x_min + 0.1, self.x_max - 0.1, self.x_steps * 10)
        self.y_new = np.linspace(self.y_min + 0.1, self.y_max - 0.1, self.y_steps * 10)
        self.X_new, self.Y_new = np.meshgrid(self.x_new, self.y_new, indexing='ij')
    
    def interpolate_response(self):
        points = np.column_stack([self.X_new.ravel(), self.Y_new.ravel()])
        grid_interpol = RegularGridInterpolator(self.grid_old, self.response, method='cubic')
        self.response_interpol = grid_interpol(points).reshape(self.X_new.shape)
        self.dx, self.dy = np.gradient(self.response_interpol, self.x_new, self.y_new)
    
    def create_plot(self):
        self.canvas.ax.plot_surface(self.X_new, self.Y_new, self.response_interpol, cmap="RdBu")
        self.canvas.ax.set_ylabel(self.y_name)
        self.canvas.ax.set_xlabel(self.x_name)

        self.annot = self.canvas.ax.text2D(0.05, 0.95, "Right-click a point to see slope", transform=self.canvas.ax.transAxes,
                                    fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

        self.canvas.fig.canvas.mpl_connect("button_press_event", self.on_mouse_click)
        self.canvas.draw()
    
    def on_click(self, event):
        return self.canvas.ax.format_coord(event.xdata, event.ydata)
    
    def on_mouse_click(self, event):
        if event.inaxes == self.cavnas.ax and event.button == 3:  # Right-click (button 3)
            if event.xdata is None or event.ydata is None:
                return
            
            coords = self.on_click(event)
            print(f"Clicked coordinates: {coords}")
            
            try:
                x_click, y_click = map(float, [s.split('=')[1] for s in coords.split(', ')[:2]])
            except ValueError:
                return

            ix = np.abs(self.x_new - x_click).argmin()
            iy = np.abs(self.y_new - y_click).argmin()
            
            slope_x = self.dx[ix, iy]
            slope_y = self.dy[ix, iy]
            response_value = self.response_interpol[ix, iy]

            self.annot.set_text(f"Selected Point: ({x_click:.2f}, {y_click:.2f})\nResponse: {response_value:.4f}\nSlope dx: {slope_x:.4f}\nSlope dy: {slope_y:.4f}")
            self.annot.set_visible(True)
            self.fig.canvas.draw_idle()
