import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def analyze_benchmark(benchmark_data):
    durations = np.array(list(benchmark_data.values()))

    average_duration = np.mean(durations)
    max_duration = np.max(durations)
    min_duration = np.min(durations)
    standard_deviation = np.std(durations)

    return {
        "Average Duration": average_duration,
        "Max Duration": max_duration,
        "Min Duration": min_duration,
        "Standard Deviation": standard_deviation
    }