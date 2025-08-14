import numpy as np

def rose_curve(theta, k: int = 2, a: float = 1.0):
    """
    r(θ) = a + sin(kθ)
    Works with scalars or numpy arrays.
    """
    return a + np.sin(k * theta)