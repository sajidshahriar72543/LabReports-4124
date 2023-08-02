import numpy as np
import scipy.signal as signal
import scipy.special as special
import math

s_attenuation_dB = int(input('Enter the stopband attenuation in dB: '))
pass_ripple_dB = int(input('Enter the passband ripple in dB: '))
trans_width = int(input('Enter the transition width in Hz: '))
sampling_freq =  int(input('Enter the sampling frequency in Hz: '))
cutoff_freq = int(input('Enter the cutoff frequency in Hz: '))

delta_P = 10 ** (pass_ripple_dB / 20) - 1
A = -20 * math.log10(delta_P)

delta_freq = trans_width / sampling_freq

N = np.ceil((A - 7.95) / (14.36 * delta_freq)).astype(int)
T = f'The Number of Filter Coefficients = {N}'
print(T)

if A <= 21:
    beta = 0
elif 21 < A < 50:
    beta = 0.5842 * (A - 21) ** 0.4 + 0.07886 * (A - 21)
else:
    beta = 0.1102 * (A - 8.7)

fc = (cutoff_freq + (trans_width / 2)) / sampling_freq
X = f'Cutoff frequency = {fc:.3e}'
print(X)

W = [special.i0(beta * np.sqrt(1 - ((2 * n / (N - 1)) ** 2))) / special.i0(beta) for n in range(N)]

Hd = np.zeros(N)
for n in range(N):
    if n == 0:
        Hd[n] = 2 * fc
    else:
        Hd[n] = (2 * fc * math.sin(n * 2 * np.pi * fc)) / (n * 2 * np.pi * fc)

print("FIR Coefficients: ")
h = [Hd[n] * W[n] for n in range(N)]
for n in range((N - 1) // 2, -1, -1):
    X = f'h[{-(n) + (N - 1) // 2}] = {h[n]:.16e} = h[{n + (N - 1) // 2}]'
    print(X)