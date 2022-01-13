'''
A algorithm that creates the Fourier transform of a given function. The base function is a rectangular
function, which has a normalized value 1 between the boundaries and 0 outside. This rectangular 
function can be multiplied whit a other given function, to create this function in between
the boundries of the rectangle.
'''

from scipy.fft import fft
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

N = 50000 # Number of samplepoints

T = 1.0 / 1000.0 # sample spacing

# position vector on lens/slit
x = np.linspace(-50, 50, N)
# x = x-2

# create a matrix with same shape as x. (x a vector so y also vector)
y = np.zeros(x.shape)

# Make stepfunction (wavefront)
for i in range(x.shape[0]):
    if x[i] > -0.5 and x[i] < 0.5: 
        y[i] = 1.0


print('''
This script by default calculates the Fourier transform of a normalized rectangular function and compares it with the sinc-function.
It is possible to calculate the Fourier transform of spherical aberration, but this will not be compared with anything.

''')

ans = input("Do you want to calculate the Fourier transform for spherical aberration? (y/n) ")

if ans == 'y':
    abb = x**4
    y = y * abb
    # Make subplot
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)


    # Plot wavefront with aberration
    ax1.plot(x,y)

    ax1.set_xlim(-2,2)
    ax1.grid()
    ax1.set_xlabel(r"x ($mm$)")
    ax1.set_ylabel(r"Waveform ($mm$)")

    # ax1.set_title(r'Waveform of light beam')


    # Fourier transform of the wavefront input
    yf = fft(y)

    # Shift Fourier transform to make it symmetrical
    yf = np.fft.fftshift(yf)
    Amp = np.abs(yf)
    Int = Amp**2


    # Calculate domain of Fourier transform
    xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

    # Plot Fourier transform
    ax2.plot(xf, Int/max(Int))

    ax2.set_xlim(-5,5)
    ax2.set_xlabel(r"$x_s$ ($mm$)")
    ax2.set_ylabel(r"$I$ ($\frac{W}{m^2})$")

    ax2.grid()
    plt.show()

else:
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)


    # Plot wavefront with aberration
    ax1.plot(x,y)

    ax1.set_xlim(-2,2)
    ax1.grid()
    ax1.set_xlabel(r"x ($mm$)")
    ax1.set_ylabel(r"Waveform ($mm$)")

    # ax1.set_title(r'Waveform of light beam')


    # Fourier transform of the wavefront input
    yf = fft(y)

    # Shift Fourier transform to make it symmetrical
    yf = np.fft.fftshift(yf)
    Amp = np.abs(yf)
    Int = Amp**2


    # Calculate domain of Fourier transform
    xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

    # Plot Fourier transform
    ax2.plot(xf, Int/max(Int))

    ax2.set_xlim(-5,5)
    ax2.set_xlabel(r"$x_s$ ($mm$)")
    ax2.set_ylabel(r"$I$ ($\frac{W}{m^2})$")

    ax2.grid()
    fig2 = plt.figure(figsize=(12,12))

    # Calculate theoratical intensity with sinc-function
    sinc = np.sinc(xf*0.5)
    sinc = sinc**2


    # Plot model and theoratical together to compare.
    ax3 = fig2.add_subplot(111)
    ax3.plot(xf, Int/max(Int), 'b-', label="Intensity Python model")
    ax3.scatter(xf, sinc/max(sinc), facecolors='none', edgecolors='r', label="Theoretical intensity")
    ax3.set_xlabel(r"$x_s$ ($mm$)")
    ax3.set_ylabel(r"$I$ ($\frac{W}{m^2})$")
    ax3.legend()
    ax3.set_xlim(-5,5)
    ax3.grid()

    plt.show()



# # Calculate aberration in the wavefront

# #abb = x**4
# y = y #* abb

# # Make subplot
# fig = plt.figure(figsize=(10,10))
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)


# # Plot wavefront with aberration
# ax1.plot(x,y)

# ax1.set_xlim(-2,2)
# ax1.grid()
# ax1.set_xlabel(r"x ($mm$)")
# ax1.set_ylabel(r"Waveform ($mm$)")

# # ax1.set_title(r'Waveform of light beam')


# # Fourier transform of the wavefront input
# yf = fft(y)

# # Shift Fourier transform to make it symmetrical
# yf = np.fft.fftshift(yf)
# Amp = np.abs(yf)
# Int = Amp**2


# # Calculate domain of Fourier transform
# xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

# # Plot Fourier transform
# ax2.plot(xf, Int/max(Int))

# ax2.set_xlim(-5,5)
# ax2.set_xlabel(r"$x_s$ ($mm$)")
# ax2.set_ylabel(r"$I$ ($\frac{W}{m^2})$")

# ax2.grid()

# ''' This next code plots the theoretical Fourier transform against the FFT algorithm. This only works for rectangular,
# because this is the only Fourier transform that has been done by hand.
# ''' 

# fig2 = plt.figure(figsize=(12,12))

# # Calculate theoratical intensity with sinc-function
# sinc = np.sinc(xf*0.5)
# sinc = sinc**2


# # Plot model and theoratical together to compare.
# ax3 = fig2.add_subplot(111)
# ax3.plot(xf, Int/max(Int), 'b-', label="Intensity Python model")
# ax3.scatter(xf, sinc/max(sinc), facecolors='none', edgecolors='r', label="Theoretical intensity")
# ax3.set_xlabel(r"$x_s$ ($mm$)")
# ax3.set_ylabel(r"$I$ ($\frac{W}{m^2})$")
# ax3.legend()
# ax3.set_xlim(-5,5)
# ax3.grid()

# plt.show()