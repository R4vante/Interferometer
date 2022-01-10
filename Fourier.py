from scipy.fft import fft
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

N = 50000 # Number of samplepoints

T = 1.0 / 1000.0 # sample spacing

x = np.linspace(-50, 50, N)
# x = x-2

y = np.zeros(x.shape)

# Make stepfunction (wavefront)
for i in range(x.shape[0]):
    if x[i] > -0.5 and x[i] < 0.5: 
        y[i] = 1.0



# Calculate aberration in the wavefront

abb = x**4
y = y * abb



# Make subplot
fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
#ax3 = fig.add_subplot(133)

# Plot wavefront with aberration
ax1.plot(x,y)

ax1.set_xlim(-2,2)
ax1.grid()
ax1.set_xlabel(r"x ($mm$)")
ax1.set_ylabel(r"Waveform ($mm$)")

ax1.set_title(r'Waveform of light beam')


# Fourier transform of the wavefront input
yf = fft(y)

# Shift Fourier transform to make it symmetrical
yf = np.fft.fftshift(yf)
Amp = np.abs(yf)
Int = Amp**2


# Calculate domain of Fourier transform
xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

#ax2.plot(x, abb)

# Plot Fourier transform
ax2.plot(xf, Int/max(Int))

plt.xlim(-5,5)
ax2.set_title('Normalized intensity spectrum')
ax2.set_xlabel(r"$x_s$ ($mm$)")
ax2.set_ylabel(r"$I$ ($\frac{W}{m^2}$")

ax2.grid()

plt.show()