import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator
from datamanager import DataManager
from loadingbar import LoadingBar
from textprocessingutilities import convert_to_underscores_from_spaces, convert_from_camel_casing_to_underscores
from guiutilities import flatten_dict

class ResponseSurface:
    def __init__(self, canvas, x_min, x_max, x_steps, y_min, y_max, y_steps, x_name, y_name, z_name, loaded_aircraft, tool_interface):
        self.canvas = canvas
        self.x_min = float(x_min)
        self.x_max = float(x_max)
        self.x_steps = int(x_steps)
        self.y_min = float(y_min)
        self.y_max = float(y_max)
        self.y_steps = int(y_steps)
        self.x_name = x_name
        self.y_name = y_name
        self.z_name = z_name
        self.loaded_aircraft = loaded_aircraft
        geometry_units_dict = flatten_dict(loaded_aircraft.geometry.push_units_to_dict())
        geometry_units_dict = {convert_from_camel_casing_to_underscores(key): unit for key, unit in geometry_units_dict.items()}
        output_units_dict = loaded_aircraft.mission_outputs.push_units_to_dict()
        self.x_units = geometry_units_dict[convert_to_underscores_from_spaces(x_name)]
        self.y_units = geometry_units_dict[convert_to_underscores_from_spaces(y_name)]
        self.z_units = output_units_dict[convert_to_underscores_from_spaces(z_name)]
        self.data_manager = DataManager(tool_interface, self.loaded_aircraft)
        
        self.initialize_grid()
        self.interpolate_response()
        self.create_plot()
    
    def compute_response(self):
        self.canvas.ax.cla()
        vx, vy = np.meshgrid(self.x, self.y, indexing='ij')
        response = np.zeros((self.x_steps, self.y_steps))
        for i, j in LoadingBar.Range((self.x_steps, self.y_steps), message='Calculating Response...'):
            x_name = self.x_name.replace(" ", "_")
            y_name = self.y_name.replace(" ", "_")
            geometry_dict = {x_name: vx[i, j], y_name: vy[i, j]}
            self.loaded_aircraft.geometry.pull_from_dict(geometry_dict)
            transfer_func_dict = self.data_manager.get_output_to_transfer_function_dict()
            z_var = convert_to_underscores_from_spaces(self.z_name)
            transfer_func_dict[z_var]()
            outputs_dict = self.loaded_aircraft.mission_outputs.push_values_to_dict()
            response[i, j] = outputs_dict[z_var]
        self.canvas.ax.scatter(vx.squeeze(), vy.squeeze(), response.squeeze(), zorder=10, alpha=1)
        return response

    def initialize_grid(self):
        self.x = np.linspace(self.x_min, self.x_max, self.x_steps)
        self.y = np.linspace(self.y_min, self.y_max, self.y_steps)
        self.response = self.compute_response()
        self.grid_old = (self.x, self.y)
        
        self.x_new = np.linspace(self.x_min, self.x_max, self.x_steps * 10)
        self.y_new = np.linspace(self.y_min, self.y_max, self.y_steps * 10)
        self.X_new, self.Y_new = np.meshgrid(self.x_new, self.y_new, indexing='ij')
    
    def interpolate_response(self):
        points = np.column_stack([self.X_new.ravel(), self.Y_new.ravel()])
        if self.response.shape[0] > 3 and self.response.shape[1] > 3:
            method = 'cubic'
        else:
            method = 'slinear'
        grid_interpol = RegularGridInterpolator(self.grid_old, self.response, method=method)
        self.response_interpol = grid_interpol(points).reshape(self.X_new.shape)
        self.dx, self.dy = np.gradient(self.response_interpol, self.x_new, self.y_new)
    
    def create_plot(self):
        z_var = convert_to_underscores_from_spaces(self.z_name)
        self.canvas.ax.plot_surface(self.X_new, self.Y_new, self.response_interpol, cmap="RdBu")
        self.canvas.ax.set_ylabel(f'{self.y_name} ({self.y_units})')
        self.canvas.ax.set_xlabel(f'{self.x_name} ({self.x_units})')
        self.canvas.ax.set_zlabel(f'{self.z_name} ({self.z_units})')

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
