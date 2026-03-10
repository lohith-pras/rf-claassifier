import numpy as np
import scipy.stats as stats


def extract_features(sample):
    i_row = sample[0, :]
    q_row = sample[1, :]
    amplitude = np.sqrt(i_row**2 + q_row**2)
    amp_mean = np.mean(amplitude)
    amp_std = np.std(amplitude)
    # Calculate skew and kurtosis of amplitude
    amp_skew = stats.skew(amplitude)
    amp_kurt = stats.kurtosis(amplitude)
    # Compute unwrapped phase
    phase = np.arctan2(q_row, i_row)
    unwrapped_phase = np.unwrap(phase)
    # Calculate phase mean and standard deviation
    phase_mean = np.mean(unwrapped_phase)
    phase_std = np.std(unwrapped_phase)
    # Differentiate the unwrapped phase to get instantaneous frequency
    inst_freq = np.diff(unwrapped_phase)
    inst_freq_mean = np.mean(inst_freq)
    inst_freq_std = np.std(inst_freq)
    # FFT of complex signal
    complex_signal = i_row + 1j * q_row
    fft_result = np.fft.fft(complex_signal)
    fft_magnitude = np.abs(fft_result)
    fft_mean = np.mean(fft_magnitude)
    fft_std = np.std(fft_magnitude)
    fft_skew = stats.skew(fft_magnitude)
    fft_kurt = stats.kurtosis(fft_magnitude)
    features = [
        amp_mean,
        amp_std,
        amp_skew,
        amp_kurt,
        phase_mean,
        phase_std,
        inst_freq_mean,
        inst_freq_std,
        fft_mean,
        fft_std,
        fft_skew,
        fft_kurt,
    ]
    return features
