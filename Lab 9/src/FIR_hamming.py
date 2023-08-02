import numpy as np
import scipy.signal as signal

def fir_coefficients_hamming(passbandFreq, trx_width, stp_bnd, sample_freq):
    passbandFreq_norm = passbandFreq / (0.5 * sample_freq)
    trx_width_norm = trx_width / (0.5 * sample_freq)

    filter_order = int(np.ceil((stp_bnd - 8 / (2.285 * np.pi * trx_width_norm))))

    if filter_order % 2 == 0:
        filter_order += 1

    filter_coeffs = signal.firwin(filter_order, passbandFreq_norm, window='hamming')

    return filter_coeffs

passband_edge_freq = int(input("Enter passband edge frequency: "))
trx_width = int(input("Enter transition width: "))
stp_bnd = int(input("Enter stopband edge frequency: "))
sample_freq = int(input("Enter sample frequency: "))

print("Hamming window: ")
print(fir_coefficients_hamming(passband_edge_freq, trx_width, stp_bnd, sample_freq))