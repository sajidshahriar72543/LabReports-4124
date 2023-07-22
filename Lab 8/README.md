## Experiment No : 08

## Submission Date : July 23, 2023

## Experiment Name :

## Experimental Study of Finding DFT of Various Functions using Matrix Method

---

## Theory:

<p style="text-align: justify">
The Discrete Fourier Transform (DFT) is a fundamental mathematical tool used to analyze signals and convert them from the time domain to the frequency domain. It is widely used in various fields such as signal processing, communications, image analysis, and audio processing. The DFT allows us to represent a discrete signal as a sum of complex exponential functions of different frequencies. [1]
</p>
<p style="text-align: justify">
For a given sequence of N complex numbers {x[0], x[1], ..., x[N-1]}, the DFT is defined as follows:
</p>

```
X[k] = sum_{n=0}^{N-1} x[n] exp(-2*pi*i*n*k/N)
```

## Code:

```python
import numpy as np
import math

def dft(x):
  N = len(x)
  n = np.arange(N)
  k = n.reshape((N,1))
  tf = np.exp(-2j*np.pi*k*n/N)

  print("\n")
  print("Twiddle Factor: ")
  print(np.round(tf, decimals=3))
  print("\n")

  return np.dot(tf,x)

if __name__ == "__main__":

  inp = int(input("Enter your choice: "))
  if inp==1:
    n = int(input("Number of elements: "))
    x = np.asarray(list(map(int, input().split())))
    for i in range (n):
      x[i] = x[i]+1
    print("DFT: ", np.round(dft(x), decimals=3))

  elif inp==2:
    n = int(input("Number of elements: "))
    x = np.asarray(list(map(int, input().split())))
    for i in range (n):
      m = math.sin(180*x[i])
      x[i] = m
    print(x)
    print("DFT: ", dft(x))

  elif inp==3:
    n = int(input("Number of elements: "))
    x = np.asarray(list(map(int, input().split())))
    for i in range (n):
      m = math.cos(180*x[i])
      x[i] = m
    print("DFT: ", dft(x))
```

## Output:

```py
Enter your choice: 1
Number of elements: 4
1 4 6 2

Twiddle Factor:
[[ 1.+0.j  1.+0.j  1.+0.j  1.+0.j]
 [ 1.+0.j  0.-1.j -1.-0.j -0.+1.j]
 [ 1.+0.j -1.-0.j  1.+0.j -1.-0.j]
 [ 1.+0.j -0.+1.j -1.-0.j  0.-1.j]]

DFT:  [17.+0.j -5.-2.j  1.+0.j -5.+2.j]
```

## Discussion and Conclusion:

<p style="text-align: justify">
All the code is implemented in python language. The output was verified with the theory. No error was faced.
</p>

## References:

[1] DFT matrix. - wikipedia, https://en.wikipedia.org/wiki/DFT_matrix (accessed Jul. 22, 2023).
