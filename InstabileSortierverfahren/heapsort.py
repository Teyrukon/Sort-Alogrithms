import big_o
from numpy import random


def heapSort(arr, log=None, iteration=None, round=None):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    size = len(arr)

    if size <= 1:
        return arr

    # Build maxheap
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        if log:
            log["HeapSort"]["Iterationen"][f"{round}"] = iteration
            iteration += 1
    return arr


if __name__ == '__main__':
    arr = random.randint(100, size=(10))
    print(heapSort(arr))
    best, other = big_o.big_o(heapSort, lambda n: big_o.datagen.integers(n, 0, 10))
    print(big_o.reports.big_o_report(best, other))
