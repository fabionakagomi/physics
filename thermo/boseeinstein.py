import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation
from numpy.fft import fft2, ifft2, fftshift
from scipy.special import hermite

"""
Bose-Einstein condensate (bose einstein BEC) for evolving Gross-Pitaevskii
equation (gross pitaevskii gpe). 
"""

class QHO:
    """
    Quantum harmonic oscillator (qho) wavefunctions.
    """
    def __init__(self, n, xshift=0, yshift=0):
        self.n = n
        self.xshift = xshift
        self.yshift = yshift
        self.E = n + 0.5
        self.coef = 1 / np.sqrt(2**n * np.factorial(n)) * (1 / np.pi)**(1/4)
        self.hermite = hermite(n)

    def __call__(self, x, y, t):
        xs = x - self.xshift
        ys = y - self.yshift
        return self.coef * np.exp(-(xs**2 + ys**2) / 2 - 1j*self.E*t) * self.hermite(x) * self.hermite(y)

class Simulation:
    """
    Simulation to step wavefunction forward in time from the given parameters
    xmax : maximum extent of boundary
    N    : number of spatial points
    init : initial wavefunction
    nonlinearity : factor in front of |psi^2| term
    """
    def __init__(self, parameters):
        self.parameters = parameters
        
        # Set up spatial dimensions.
        xmax = parameters["xmax"]
        self.xmax = xmax
        N = parameters["N"]
        v = linspace(-xmax, xmax, N)
        self.dx = v[1] - v[0]
        self.x, self.y = np.meshgrid(v, v)

        # Spectral space.
        kmax = 2*np.pi / self.dx
        dk = kmax / N
        self.k = np.fft.fftshift((arange(N)-N/2) * dk)
        kx, ky = np.meshgrid(self.k, self.k)
