def radixSort(arr, log=None, iteration=None, round=None):
    maxNum = max(arr)
    bitLen = maxNum.bit_length()
    bins = [[], []]

    for j in range(bitLen):
        binCount = [0, 0]
        for k in range(len(arr)):
            bitValue = (arr[k] >> j) & 1
            bins[bitValue].append(arr[k])
            binCount[bitValue] += 1
        index = 0
        for bit in range(2):
            for i in range(binCount[bit]):
                arr[index] = bins[bit][i]
                index += 1
            if log:
                log["RadixSort"]["Iterationen"][f"{round}"] = iteration
                iteration += 1
        bins = [[], []]
    return arr
