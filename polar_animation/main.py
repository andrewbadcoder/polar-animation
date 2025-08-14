import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from polar_animation.plotter import animate_polar
from functions import rose_curve
import numpy as np

if __name__ == "__main__":
    # Example: r = 1 + sin(5θ)
    animate_polar(lambda t: rose_curve(t, k=5, a=0), theta_max=2*np.pi, samples=800, interval=16)