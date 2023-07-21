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
    print(np.round(fft(x_final), decimals=2))