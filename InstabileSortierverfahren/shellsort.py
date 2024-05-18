def shellSort(arr, log=None, iteration=None, round=None):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            if log:
                log["ShellSort"]["Iterationen"][f"{round}"] = iteration
                iteration += 1  # Iterationszähler erhöhen
        gap //= 2
    return arr
