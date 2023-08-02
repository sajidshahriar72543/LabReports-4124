## Experiment No : 09

## Submission Date : August 05, 2023

## Experiment Name :

## Experimental study of calculating FIR coefficient using Hamming and Kaiser window method.

---

## Theory:

<p style="text-align: justify">
The Hamming window is a popular windowing function used in digital signal processing. It is used to design an n-th order lowpass, bandpass, or multiband FIR filter with linear phase. The filter type depends on the number of elements of Wn. If you do not specify a window, fir1 applies a Hamming window [1]
</p>

<p style="text-align: justify">
The Kaiser window is another popular windowing function used in digital signal processing. The kaiserord function estimates the filter order, cutoff frequency, and Kaiser window beta parameter needed to meet a given set of specifications [1]
</p>

## Code:

### Hamming Window

```python
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
```

## Output:

```py
Enter passband edge frequency: 1000
Enter transition width: 200
Enter stopband edge frequency: 60
Enter sample frequency: 8000
Hamming window:
[ 9.45280056e-04  1.52175778e-03  1.38563968e-03 -1.31656882e-18
 -2.64907799e-03 -5.18087531e-03 -4.98060163e-03  3.45292786e-18
  8.71640252e-03  1.59387590e-02  1.44178098e-02 -6.34676108e-18
 -2.32451422e-02 -4.18881839e-02 -3.82352571e-02  8.77768409e-18
  7.06856817e-02  1.54791656e-01  2.23095520e-01  2.49361263e-01
  2.23095520e-01  1.54791656e-01  7.06856817e-02  8.77768409e-18
 -3.82352571e-02 -4.18881839e-02 -2.32451422e-02 -6.34676108e-18
  1.44178098e-02  1.59387590e-02  8.71640252e-03  3.45292786e-18
 -4.98060163e-03 -5.18087531e-03 -2.64907799e-03 -1.31656882e-18
  1.38563968e-03  1.52175778e-03  9.45280056e-04]
```

### Kaiser Window

```python
import numpy as np
from scipy import signal

def fir_coefficients_kaiser(passbandFreq, trx_width, stp_bnd, sample_freq, beta):
    passbandFreq_norm = passbandFreq / (0.5 * sample_freq)
    trx_width_norm = trx_width / (0.5 * sample_freq)

    filter_order = int(np.ceil((stp_bnd - 8) / (2.285 * np.pi * trx_width_norm)))

    if filter_order % 2 == 0:
        filter_order += 1

    filter_coeffs = signal.firwin(filter_order, passbandFreq_norm, window=('kaiser', beta))

    return filter_coeffs

passband_edge_freq = int(input("Enter passband edge frequency: "))
trx_width = int(input("Enter transition width: "))
stp_bnd = int(input("Enter stopband edge frequency: "))
sample_freq = int(input("Enter sample frequency: "))
beta = float(input("Enter Kaiser window parameter (beta): "))

print("Kaiser window: ")
print(fir_coefficients_kaiser(passband_edge_freq, trx_width, stp_bnd, sample_freq, beta))
```
```py
FIR Coefficients:
h[0] = 9.5158015973554252e-05 = h[70]
h[1] = -1.3568629971363779e-04 = h[69]
h[2] = -4.4285715067774996e-04 = h[68]
h[3] = -4.7648717852728307e-04 = h[67]
h[4] = 2.5638811520526608e-05 = h[66]
h[5] = 8.5050212677058789e-04 = h[65]
h[6] = 1.2750327327541232e-03 = h[64]
h[7] = 6.0748283253907903e-04 = h[63]
h[8] = -1.0300599798411913e-03 = h[62]
h[9] = -2.4336299788426043e-03 = h[61]
h[10] = -2.0819018922964877e-03 = h[60]
h[11] = 4.3912062199009721e-04 = h[59]
h[12] = 3.5617442010633816e-03 = h[58]
h[13] = 4.5141376899528957e-03 = h[57]
h[14] = 1.5801009808523864e-03 = h[56]
h[15] = -3.8639107019382327e-03 = h[55]
h[16] = -7.5932106559318552e-03 = h[54]
h[17] = -5.5757902574872916e-03 = h[53]
h[18] = 2.1905368603566057e-03 = h[52]
h[19] = 1.0406117790206308e-02 = h[51]
h[20] = 1.1716770174941061e-02 = h[50]
h[21] = 2.8150021613893967e-03 = h[49]
h[22] = -1.1349529877834660e-02 = h[48]
h[23] = -1.9586511559541352e-02 = h[47]
h[24] = -1.2641473278390585e-02 = h[46]
h[25] = 7.9934616345173591e-03 = h[45]
h[26] = 2.8146661713456561e-02 = h[44]
h[27] = 2.9444288298591612e-02 = h[43]
h[28] = 3.8695033434914682e-03 = h[42]
h[29] = -3.5922008549826252e-02 = h[41]
h[30] = -5.9743424772903737e-02 = h[40]
h[31] = -3.7104296227502512e-02 = h[39]
h[32] = 4.1372225270762092e-02 = h[38]
h[33] = 1.5290336291807857e-01 = h[37]
h[34] = 2.5100241798626927e-01 = h[36]
h[35] = 2.8999999999999998e-01 = h[35]
```

## Discussion and Conclusion:

<p style="text-align: justify">
All the code is implemented in python language. The output was verified with the theory. No error was faced.
</p>

## References:

[1] Window-based FIR filter design - MATLAB, https://www.mathworks.com/help/signal/ref/fir1.html (accessed Aug. 2, 2023).
