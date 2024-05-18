def mergeSort(arr, log=None, iteration=None, round=None):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        mergeSort(left, log, iteration, round)
        mergeSort(right, log, iteration, round)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            if log:
                log["MergeSort"]["Iterationen"][f"{round}"] = iteration
                iteration += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            if log:
                log["MergeSort"]["Iterationen"][f"{round}"] = iteration
                iteration += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            if log:
                log["MergeSort"]["Iterationen"][f"{round}"] = iteration
                iteration += 1
    return arr
