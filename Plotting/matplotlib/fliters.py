from numpy import array, ones

from scipy import zeros
from scipy.signal import butter, impulse, lfilter, lfilter_zi, freqz, firwin

from pylab import log10, unwrap, arctan2, imag, real, repeat, arange

import matplotlib.pyplot as plt


class FilterWork:
    def __init__(self):
        pass

    # Plot frequency and phase response
    @staticmethod
    def mfreqz(b, a=1):
        w, h = freqz(b, a)
        h_db = 20 * log10(abs(h))
        plt.subplot(211)
        plt.plot(w/max(w), h_db)
        plt.ylim(-150, 5)
        plt.ylabel('Magnitude (db)')
        plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
        plt.title(r'Frequency response')
        plt.subplot(212)
        h_phase = unwrap(arctan2(imag(h), real(h)))
        plt.plot(w/max(w), h_phase)
        plt.ylabel('Phase (radians)')
        plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
        plt.title(r'Phase response')
        plt.subplots_adjust(hspace=0.5)

    # Plot step and impulse response
    # @staticmethod
    # def impz(b, a=1):
    #     l_ = len(b)
    #     impulse_ = repeat(0., l_)
    #     impulse_[0] = 1.
    #     x = arange(0, l_)
    #     response = signal.lfilter(b, a, impulse_)
    #     subplot(211)
    #     stem(x, response)
    #     ylabel('Amplitude')
    #     xlabel(r'n (samples)')
    #     title(r'Impulse response')
    #     subplot(212)
    #     step = cumsum(response)
    #     stem(x, step)
    #     ylabel('Amplitude')
    #     xlabel(r'n (samples)')
    #     title(r'Step response')
    #     subplots_adjust(hspace=0.5)


fltr = FilterWork()

b1, a1 = butter(4, [1.5 / 678, 15.0 / 678], 'bandpass')

fltr.mfreqz(b1)
plt.show()

# Highpass FIR Filter
n = 101
hpf = firwin(n, cutoff=0.3, window='hanning', pass_zero=False)
fltr.mfreqz(hpf)
plt.show()


#
# # Gives samples of the continuous-time impulse response.  You are looking for the discrete-time impulse response.
# T, h1 = impulse((b1, a1))
# plt.plot(T, h1)
# plt.show()
#
# # The function is not directly available.   However, you can get it (minus the auto-compute N part), using
# N = 100
# x = zeros(N)
# x[0] = 1
# h1 = lfilter(b1, a1, x)
# plt.plot(T, h1)
# plt.show()


#
#
# >> > from scipy.signal import lfilter, lfilter_zi, butter
# >> > b, a = butter(5, 0.25)
# >> > zi = lfilter_zi(b, a)
# >> > y, zo = lfilter(b, a, ones(10), zi=zi)
# >> > y
# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
