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
    f = 100e-2  # focal length of positive lens

    tx = 0.0e-3;ty = 0.0e-3  # tilt of mirror 1
    tx_list = np.linspace(-2.0e-3, 2.0e-3, 5)
    grid_height = 1
    grid_width = 5

    def run_normal():
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        light_beam.disturb(tx, ty)
        light_beam.interfere()
        light_beam.plot()
        plt.show()

    def my_subplot(my_grid_width, my_grid_height, my_tx_list):
        light_beam = Michelson(wavelength, size, N, R, z1, z2, z3, z4, Rbs, f)
        i = 0
        fig = plt.figure()

        for my_tx in my_tx_list:
            i += 1
            light_beam.disturb(my_tx, 0)
            light_beam.interfere()
            I = light_beam.get_intensity()
            fig.add_subplot(my_grid_height, my_grid_width, i).imshow(I, cmap="gray")
            plt.axis("off")
            light_beam.reset_tilt(my_tx, 0)

        plt.show()

    # run_normal()
    my_subplot(grid_width, grid_height, tx_list)


if __name__ == "__main__":
    main()
