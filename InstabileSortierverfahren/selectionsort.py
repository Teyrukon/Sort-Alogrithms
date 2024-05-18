import random

import big_o
from numpy import random


def selectionSort(arr, log=None, iteration=None, round=None):
    if len(arr) <= 1:
        return arr
    size = len(arr)
    for i in range(size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # swap
        if log:
            log["SelectionSort"]["Iterationen"][f"{round}"] = iteration
            iteration += 1
    return arr


if __name__ == '__main__':
    arr = random.randint(100, size=(10))
    print(selectionSort(arr))
    best, other = big_o.big_o(selectionSort, lambda n: big_o.datagen.integers(n, 0, 10), max_n=10000)
    print(big_o.reports.big_o_report(best, other))