import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_polar(func, theta_max=2*np.pi, samples=1000, interval=16):
    """
    Animate a polar function r = func(theta) on a polar axis.

    Parameters
    ----------
    func : callable
        Accepts theta (scalar or ndarray), returns r of same shape.
    theta_max : float
        Max angle to draw up to (default 2π).
    samples : int
        Total resolution of the curve.
    interval : int
        Frame interval in ms (smaller = faster animation).
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    theta = np.linspace(0, theta_max, samples)
    r_full = func(theta)

    (line,) = ax.plot([], [], lw=2)
    ax.set_title("Polar Animation", pad=20)

    def init():
        line.set_data([], [])
        return (line,)

    def update(frame):
        line.set_data(theta[:frame], r_full[:frame])
        return (line,)

    ani = FuncAnimation(fig, update, frames=samples, init_func=init, blit=True, interval=interval)
    plt.show()