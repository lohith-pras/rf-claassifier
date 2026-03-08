import pickle
import matplotlib.pyplot as plt


def plot_iq(sample):
    i_row = sample[0, :]
    q_row = sample[1, :]
    x = range(len(i_row))
    fig, axs = plt.subplots(2)
    plt.suptitle("I and Q components")
    axs[0].plot(x, i_row)
    axs[0].set_xlabel("Sample Index")
    axs[0].set_ylabel("Amplitude")
    axs[1].plot(x, q_row)
    axs[1].set_xlabel("Sample Index")
    axs[1].set_ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
