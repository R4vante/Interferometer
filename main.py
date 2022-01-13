import numpy as np
from Michelson import Michelson
import matplotlib.pyplot as plt


def main():
    wavelength = 632.8e-9  # wavelength of HeNe laser
    size = 20e-3  # size of the grid
    N = 5000  # number (NxN) of grid pixels
    R = 5e-3  # laser beam radius
    z1 = 8e-2  # length of arm 1
    z2 = 3.6e-2 + wavelength/2  # length of arm 2
    z3 = 3e-2  # distance laser to beam splitter
    z4 = 5e-2  # distance beam splitter to screen
    Rbs = 0.5  # reflection beam splitter
    f = 100e-3  # focal length of positive lens
    #f = 100e-2

    tx = 2.0e-3; ty = 0.0e-3  # tilt of mirror 1
    tx_list = np.linspace(-2.0e-3, 2.0e-3, 5)
    ty_list = np.linspace(-2.0e-3, 2.0e-3, 5)
    grid_height = 2
    grid_width = 5

    # Initial function to create tip and tillt.
    def run_normal():
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        light_beam.tilt(tx, ty)
        light_beam.interfere()
        light_beam.plot()
        plt.show()

    def my_subplot(my_grid_width, my_grid_height, my_tx_list, my_ty_list):
        i = 0

        # first figure
        fig1 = plt.figure()

        # subplots in x direction
        for my_tx in my_tx_list:
            i += 1
            light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
            light_beam.tilt(my_tx, 0)
            light_beam.interfere()
            light_beam.subplot(my_grid_width, my_grid_height, my_tx, args=i)

        # subplots in y direction
        for my_ty in my_ty_list:
            i += 1
            light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
            light_beam.tilt(0, my_ty)
            light_beam.interfere()
            I = light_beam.get_intensity()
            light_beam.subplot(my_grid_width, my_grid_height, my_ty, args=i)

    # Function that is called now. Creates spherical aberration of any kind by zernike coefficients.
    def spherical_aberration(n, m, tx, ty):
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        light_beam.spherical(n, m)
        light_beam.tilt(tx, ty)
        light_beam.interfere()
        light_beam.plot_intensity()
        light_beam.plot()


    # Function call
    spherical_aberration(2, 2, 0e-3, 0)

    plt.show()


if __name__ == "__main__":
    main()
