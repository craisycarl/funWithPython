from pylab import subplot, plot, ylim, ylabel, xlabel, title, subplots_adjust, show
from pylab import log10, unwrap, arctan2, imag, real, repeat, arange, stem, cumsum

import scipy.signal as signal


def mfreqz(b, a=1):
    w, h = signal.freqz(b, a)
    h_db = 20 * log10(abs(h))
    subplot(211)
    plot(w/max(w), h_db)
    ylim(-150, 5)
    ylabel('Magnitude (db)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Frequency response')
    subplot(212)
    h_phase = unwrap(arctan2(imag(h), real(h)))
    plot(w/max(w), h_phase)
    ylabel('Phase (radians)')
    xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    title(r'Phase response')
    subplots_adjust(hspace=0.5)
    show()


def impz(b, a=1):
    impulse = repeat(0., 50)
    impulse[0] = 1.
    x = arange(0, 50)
    response = signal.lfilter(b, a, impulse)
    subplot(211)
    stem(x, response)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')
    subplot(212)
    step = cumsum(response)
    stem(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')
    subplots_adjust(hspace=0.5)
    show()


b_, a_ = signal.iirdesign(wp=[0.05, 0.3], ws=[0.02, 0.35], gstop=60, gpass=1, ftype='ellip')
mfreqz(b_, a_)
impz(b_, a_)
