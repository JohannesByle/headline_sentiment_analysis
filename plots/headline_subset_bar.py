import matplotlib.pyplot as plt
from textblob import Sentence
import numpy as np


def compare_subsets(data, subset_1, subset_2, bin_count=10, color_1="red", color_2="blue"):
    subset_data_1 = []
    subset_data_2 = []

    for sentence in data:
        for term in subset_1:
            if term.upper() in sentence.upper():
                subset_data_1.append(Sentence(sentence).polarity)
        for term in subset_2:
            if term.upper() in sentence.upper():
                subset_data_2.append(Sentence(sentence).polarity)

    hist, bins = np.histogram(subset_data_1 + subset_data_2, bins=bin_count)
    hist_1, _ = np.histogram(subset_data_1, bins=bins)
    hist_2, _ = np.histogram(subset_data_2, bins=bins)
    bins = np.asarray([bins[n] + (bins[n + 1] + bins[n]) / 2 for n in range(len(bins) - 1)])
    width = ((max(bins) - min(bins)) / len(bins)) / 2
    plt.bar(bins - width / 2, hist_1, color=color_1, width=width, label=", ".join(subset_1))
    plt.bar(bins + width / 2, hist_2, color=color_2, width=width, label=", ".join(subset_2))
    plt.xlabel("Polarity")
    plt.ylabel("Number of Articles")
    plt.legend()
