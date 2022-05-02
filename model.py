import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.fftpack import *


def hilbert_1(signal):
	N = len(signal)
	U = fft(signal)

	M = N - N//2 - 1
	U[N//2+1:] = [0] * M
	U[1:N//2] = 2 * U[1:N//2]

	v = ifft(U)
	return v

def derivative(f, dx):
	df = []
	df.append((f[1] - f[0]) / dx)
	
	for i in range(1, len(f)):
		df.append((f[i] - f[i - 1]) / dx)

	return df


def ort_signal(signal):
	h = hilbert_1(signal)
	ort_signal = []

	for i in range(0, len(signal)):
		ort_signal.append(h[i].imag)
	
	return ort_signal


def analitic_signal(signal):
	analitic_signal = []
	h = hilbert_1(signal)
	ort_signal = []

	for i in range(0, len(signal)):
		ort_signal.append(h[i].imag)

	for i in range(0, len(signal)):
		analitic_signal.append(complex(signal[i], ort_signal[i]))

	return analitic_signal


def smoothing(signal, K):
	new_signal = [0] * len(signal)

	for i in range(K, len(signal) - K):
		for j in range(-K, K):
			new_signal[i] += signal[i + j] / (2*K + 1)
	return new_signal


def amp(signal):
	return np.abs(signal)


def cap(signal):
	return np.abs(signal) * np.abs(signal)


def frq(signal, dx):
	u = [x.real for x in signal]
	v = [x.imag for x in signal]
	freeq = []

	for i in range(0, len(signal)):
		freeq.append(m.asin(v[i] / np.abs(signal[i])))
		# if u[i] != 0:
		# 	freeq.append(m.atan(v[i] / u[i]))
		# else:
		# 	freeq.append(m.atan(m.pi / 2))

	return np.abs(derivative(freeq, dx))
#-------------------------------------

# d = 10
# discr = 0.0008
# l = int(d / discr)

# axis = [(x * 0.0008) for x in range(0, l)]
# signal = [m.sin(x) for x in axis]

# ort_signal = ort_signal(signal)
# analitic_signal = analitic_signal(signal)

# plt.axis([0, d, -2.5, 2.5])

# plt.plot(axis, signal)
# plt.plot(axis, ort_signal, color = 'red')

# # plt.plot(axis, amp(analitic_signal))
# # plt.plot(axis, cap(analitic_signal))
# # plt.plot(axis, smoothing( frq(analitic_signal, 0.0008), 50), color = 'grey')

# plt.show()


