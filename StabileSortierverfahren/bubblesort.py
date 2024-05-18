import big_o
from numpy import random


def bubbleSort(arr, log=None, iteration=None, round=None):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                if log:
                    log["BubbleSort"]["Iterationen"][f"{round}"] = iteration
                    iteration += 1
    return arr

if __name__ == '__main__':
    arr = random.randint(100, size=(10))
    print(bubbleSort(arr))
    best, other = big_o.big_o(bubbleSort, lambda n: big_o.datagen.integers(n, 0, 10), verbose=True)
    print(big_o.reports.big_o_report(best, other))