import matplotlib.pyplot as plt
import numpy as np
from LightPipes import *


class Michelson:

    def __init__(self, wavelength, grid, gridpoints, Radius, arm1, arm2, armBS, armScreen, Reflection, focal):
        self.wavelength = wavelength  # wavelength of HeNe laser
        self.size = grid  # size of the grid
        self.N = gridpoints  # number (NxN) of grid pixels
        self.R = Radius  # laser beam radius
        self.z1 = arm1  # length of arm 1
        self.z2 = arm2  # length of arm 2
        self.z3 = armBS  # distance laser to beamsplitter
        self.z4 = armScreen  # distance beamsplitter to screen
        self.Rbs = Reflection  # reflection beam splitter
        self.f = focal  # focal length of positive lens
        self.A = wavelength / (2 * np.pi)
        self.I = 0  # intensity

        # Generate a weak converging laser beam using a weak positive lens
        self.F = GaussHermite(Begin(self.size, self.wavelength, self.N), self.R)

    def tilt(self, tx, ty):
        # Introduces tilt to the beam, before it enters the interferometer
        self.F = CircAperture(self.size/3, 0, 0, self.F)
        self.F = Tilt(tx, ty, self.F)

        """ Create an aberration with Zernike function (n=4, m=0)"""

    def interfere(self):
        self.F = Lens(self.f, 0, 0, self.F)

        # Propagate to the beam splitter:
        self.F = Forvard(self.z3, self.F)

        # Split the beam and propagate to- and back from mirror #2:
        F2 = IntAttenuator(1-self.Rbs, self.F)
        F2 = Forvard(self.z2, F2)

        F2 = IntAttenuator(self.Rbs, F2)

        # Split off the second beam and propagate to- and back from the mirror #1:
        F10 = IntAttenuator(self.Rbs, self.F)
        F1 = Forvard(self.z1*2, F10)
        F1 = IntAttenuator(1-self.Rbs, F1)

        # Recombine the two beams and propagate to the screen:
        self.F = BeamMix(F1, F2)
        self.F = Forvard(self.z4, self.F)
        self.I = Intensity(1, self.F)

    def reset_tilt(self, current_tx, current_ty):
        # tilting the wavefront back to a straight wavefront
        self.F = CircAperture(self.size/3, 0, 0, self.F)
        self.F = Tilt(-current_tx, -current_ty, self.F)

    def plot(self):
        plt.figure()
        plt.imshow(self.I, cmap='gray')
        plt.axis('off')
        plt.title('intensity pattern')

    def subplot(self, grid_width, grid_height, tilt, args):
        plt.subplot(grid_height, grid_width, args).imshow(self.I, cmap='gray')
        plt.axis("off")
        plt.title("Tilt: %.1E" % tilt)

    def get_intensity(self):
        return self.I

    def spherical(self):
        A = self.wavelength/(2*np.pi*np.sqrt(6))
        self.F = CircAperture(self.size / 3, 0, 0, self.F)
        self.F = Zernike(1, 1, self.size/3, 10*A, self.F)

    def plot_intensity(self):
        plt.figure()
        x = np.linspace(-self.size/2, self.size/2, self.N)
        plt.plot(x, self.I[int(self.N/2)])
