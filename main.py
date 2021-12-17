import numpy as np

from Michelson import Michelson
import matplotlib.pyplot as plt

# MAIN
def main():
    wavelength = 632.8e-9  # wavelength of HeNe laser
    size = 30e-3  # size of the grid
    N = 900  # number (NxN) of grid pixels
    R = 3e-3  # laser beam radius
    z1 = 8e-2  # length of arm 1
    z2 = 3.6e-2  # length of arm 2
    z3 = 3e-2  # distance laser to beamsplitter
    z4 = 5e-2  # distance beamsplitter to screen
    Rbs = 0.5  # reflection beam splitter
    f = -100e-2  # focal length of positive lens

    tx = 0.0e-3;ty = 0.0e-3  # tilt of mirror 1
    tx_list = np.linspace(-2.0e-3, 2.0e-3, 5)
    ty_list = np.linspace(-2.0e-3, 2.0e-3, 5)
    grid_height = 2
    grid_width = 5

    def run_normal():
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        light_beam.disturb(tx, ty)
        light_beam.interfere()
        light_beam.plot()
        plt.show()

    def my_subplot(my_grid_width, my_grid_height, my_tx_list, my_ty_list):
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        i = 0

        # first figure
        fig1 = plt.figure()

        # subplots in x direction
        for my_tx in my_tx_list:
            i += 1
            light_beam.disturb(my_tx, 0)
            light_beam.interfere()
            I = light_beam.get_intensity()
            light_beam.subplot_x(my_grid_width, my_grid_height, my_tx, args=i)
            light_beam.reset_tilt(my_tx, 0)

        # subplots in y direction
        for my_ty in my_ty_list:
            i += 1
            light_beam.disturb(0, my_ty)
            light_beam.interfere()
            I = light_beam.get_intensity()
            light_beam.subplot_y(my_grid_width, my_grid_height, my_ty, args=i)
            light_beam.reset_tilt(0, my_ty)
        #plt.show()

    # run_normal()

    # Plot for tilt in x direction
    # Create figure
    my_subplot(grid_width, grid_height, tx_list, ty_list)

    # Plot for tilt in y direction
    plt.show()


if __name__ == "__main__":
    main()
