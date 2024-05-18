def quickSort(arr, log=None, iteration=None, round=None):
    # Basisfall: Ein Array mit einer Länge von 0 oder 1 ist bereits sortiert
    if len(arr) <= 1:
        return arr
    if log:
        log["QuickSort"]["Iterationen"][f"{round}"] = iteration
        iteration += 1
    # Wähle ein Pivot-Element, hier das mittlere Element des Arrays
    pivot = arr[len(arr) // 2]
    # Teile das Array in drei Teile: Elemente kleiner als der Pivot,
    # Elemente gleich dem Pivot und Elemente größer als der Pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Rekursive Aufrufe für die linke und rechte Partition und Kombinieren der Ergebnisse
    return quickSort(left, log, iteration, round) + middle + quickSort(right, log, iteration, round)
