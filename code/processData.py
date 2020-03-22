from scipy import signal



def processing(in_signal):

    bh, ah = signal.butter(4, 0.02, 'high')
    out_signal = signal.filtfilt(bh, ah, in_signal)

    return out_signal

