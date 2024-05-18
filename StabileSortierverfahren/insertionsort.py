def insertionSort(arr, log=None, iteration=None, round=None):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        if log:
            log["InsertionSort"]["Iterationen"][f"{round}"] = iteration
            iteration += 1
    return arr