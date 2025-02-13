import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator

class ResponseSurfaceGenerator:
    def __init__(self, x_min, x_max, x_steps, y_min, y_max, y_steps, x_name, y_name, r_name):
        self.x_min = x_min
        self.x_max = x_max
        self.x_steps = x_steps
        self.y_min = y_min
        self.y_max = y_max
        self.y_steps = y_steps
        self.x_name = x_name
        self.y_name = y_name
        self.r_name = r_name

        self.x_values = np.linspace(self.x_min, self.x_max, self.x_steps)
        self.y_values = np.linspace(self.y_min, self.y_max, self.y_steps)
        self.X, self.Y = np.meshgrid(self.x_values, self.y_values)
        self.R = np.zeros_like(self.X)

    def compute_response(self):
        for i in range(self.x_steps):
            for j in range(self.y_steps):
                update_inputs(self.X[j, i], self.Y[j, i], self.x_name, self.y_name)
                self.R[j, i] = get_response(self.r_name)

    def normalize_data(self):
        X_norm = (self.X - self.x_min) / (self.x_max - self.x_min)
        Y_norm = (self.Y - self.y_min) / (self.y_max - self.y_min)
        R_min, R_max = np.min(self.R), np.max(self.R)
        R_norm = (self.R - R_min) / (R_max - R_min) if R_max != R_min else self.R
        return X_norm, Y_norm, R_norm

    def interpolate_response(self):
        interpolator = RegularGridInterpolator((self.x_values, self.y_values), self.R, method='cubic')
        x_new = np.linspace(self.x_min + 0.1, self.x_max - 0.1, self.x_steps * 10)
        y_new = np.linspace(self.y_min + 0.1, self.y_max - 0.1, self.y_steps * 10)
        grid_new = np.meshgrid(x_new, y_new)
        grid_flattened = np.transpose(np.array([k.flatten() for k in grid_new]))
        R_interpolated = interpolator(grid_flattened)
        R_new = R_interpolated.reshape(len(x_new), len(y_new))
        return grid_new, R_new

    def plot_response_surface(self):
        grid_new, R_new = self.interpolate_response()

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(grid_new[0], grid_new[1], R_new.T, cmap='viridis', edgecolor='k')

        ax.set_xlabel(f"Normalized {self.x_name} (0 to 1)")
        ax.set_ylabel(f"Normalized {self.y_name} (0 to 1)")
        ax.set_zlabel(f"Normalized {self.r_name} (0 to 1)")
        ax.set_title(f"Interpolated Response Surface for {self.r_name}")

        plt.show()

    def generate(self):
        self.compute_response()
        self.plot_response_surface()

    def random_surface()
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.interpolate import RegularGridInterpolator
        from mpl_toolkits.mplot3d import Axes3D

        vel = np.random.random((21, 30))

        x = np.arange(0, 21, 1)
        y = np.arange(0, 30, 1)
        grid_old = (x, y)

        x_new = np.arange(0.1, 19.9, 0.1)
        y_new = np.arange(0.1, 28.9, 0.1)
        X_new, Y_new = np.meshgrid(x_new, y_new, indexing='ij')
        points = np.column_stack([X_new.ravel(), Y_new.ravel()])
        grid_interpol = RegularGridInterpolator(grid_old, vel, method='cubic')
        vel_interpol = grid_interpol(points).reshape(X_new.shape)
        dx, dy = np.gradient(vel_interpol, x_new, y_new)

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X_new, Y_new, vel_interpol, cmap="RdBu")

        annot = ax.text2D(0.05, 0.95, "Right-click a point to see slope", transform=ax.transAxes,
                        fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

        def on_mouse_click(event):
            if event.inaxes == ax and event.button == 3:  # Right-click (button 3)
                if event.xdata is None or event.ydata is None:
                    return

                x_click, y_click = event.xdata, event.ydata

                ix = np.abs(x_new - x_click).argmin()
                iy = np.abs(y_new - y_click).argmin()

                slope_x = dx[ix, iy]
                slope_y = dy[ix, iy]

                annot.set_text(f"Slope dx: {slope_x:.4f}\nSlope dy: {slope_y:.4f}")

                fig.canvas.draw_idle()

        fig.canvas.mpl_connect("button_press_event", on_mouse_click)

        plt.show()
