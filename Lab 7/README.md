## Experiment No : 07

## Submission Date : July 16, 2023

## Experiment Name :

## Implementation of Fast Time Fourier Transform using Butterfly Algorithm

---

## Theory:

<p style="text-align: justify">
Fast fourier transform is an algorithm which is used to compute the discrete fourier transform of a sequence. It is a divide and conquer algorithm which recursively divides the sequence into two halves and then computes the DFT of the sequence. Butterfly algorithm is used to compute the DFT of the sequence. It is faster than the DFT algorithm as it reduces the number of computations. [1]
</p>

## Code:

```python
import numpy as np

def fft(x):
    N = len(x)
    
    if N == 1:
        return x
    
    evn = fft(x[::2])
    odd = fft(x[1::2])
    
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([evn + factor[:N//2] * odd,
                           evn + factor[N//2:] * odd])

if __name__ == "__main__":

    print("Enter the list: ")
    x = np.asarray(list(map(int,input().split())))

    rev_x = np.flip(x)
    x_final = np.concatenate((x, rev_x))

    print("Input Signal:")
    print(x_final)
    
    print("\nFFT Output:")
    print(np.round(fft(x_final), decimals=3))
```
<br><br>
## Output:
```py
Enter the list: 
1 2 3 4
Input Signal:
[1 2 3 4 4 3 2 1]

FFT Output:
[20.   +0.j    -5.828-2.414j -0.   -0.j    -0.172-0.414j  0.   -0.j -0.172+0.414j  0.   -0.j    -5.828+2.414j]
```

## Discussion and Conclusion:

<p style="text-align: justify">
All the code is implemented in python language. The output was verified with the theory. No error was faced.
</p>

## References:

[1] Example of an 8 point FFT butterfly scheme. - researchgate, https://www.researchgate.net/figure/Example-of-an-8-point-FFT-butterfly-scheme_fig4_260614553 (accessed Jul. 13, 2023). 
