import threading
import time

import big_o
from datetime import datetime
from random import randint

import numpy as np
from tabulate import tabulate

from GLOBALS import *
from InstabileSortierverfahren.heapsort import heapSort
from InstabileSortierverfahren.quicksort import quickSort
from InstabileSortierverfahren.shellsort import shellSort
from InstabileSortierverfahren.selectionsort import selectionSort

from StabileSortierverfahren.bubblesort import bubbleSort
from StabileSortierverfahren.insertionsort import insertionSort
from StabileSortierverfahren.mergesort import mergeSort
from StabileSortierverfahren.radixsort import radixSort

benchmark = []
benchmarkHeader = []
benchmarkStatus = None
benchmarkDone = False

demoTbl = []
demoHeader = [f"{BOLDPREFIX}Algorithm{SUFFIX}", f"{BOLDPREFIX}Elements{SUFFIX}", f"{BOLDPREFIX}Duration (µs){SUFFIX}"]
demoLog = {}
demoDone = False


def benchmarkTask():
    def O(name: big_o.complexities.ComplexityClass):
        comp = big_o.complexities
        if isinstance(name, comp.Constant):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(1)"
        elif isinstance(name, comp.Linear):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(n)"
        elif isinstance(name, comp.Quadratic):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(n²)"
        elif isinstance(name, comp.Cubic):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(n³)"
        elif isinstance(name, comp.Polynomial):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(nᵏ)"
        elif isinstance(name, comp.Logarithmic):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(log n)"
        elif isinstance(name, comp.Linearithmic):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(n log n)"
        elif isinstance(name, comp.Exponential):
            return f"{name.__class__.__name__} {ITALICPREFIX}O{SUFFIX}(2ⁿ)"
        else:
            return f"{name.__class__.__name__}"

    global benchmark, benchmarkHeader, benchmarkStatus, benchmarkDone

    global demoLog, demoAlogReady

    base = 125
    maximum = base ** 2
    ### Instabile Sortierverfahren
    tbl = []
    header = [f"{BOLDPREFIX}Algorithm{SUFFIX}", f"{BOLDPREFIX + REDPREFIX}Duration (µs) (worst){SUFFIX + SUFFIX}",
              f"{BOLDPREFIX + GREENPREFIX}Duration (µs) (best){SUFFIX + SUFFIX}", f"{BOLDPREFIX}Complexity{SUFFIX}"]
    ## QuickSort
    algo = "QuickSort"
    index = 1
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(quickSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append([algo, 0, 0,
                f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
                f"Theoretisch:{SUFFIX}\nBest Case: O(n log n)\nWorst Case: O(n²)"])

    ## HeapSort
    algo = "HeapSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(heapSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append(
        [algo, 0, 0, f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}Theoretisch:{SUFFIX} O(n log n)"])

    ## SelectionSort
    algo = "SelectionSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(selectionSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append([algo, 0, 0,
                f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
                f"Theoretisch:{SUFFIX}\nBest Case: O(N log n)\nAverage Case: O(n log "
                f"n)\nWorst Case: O(n²)"])

    ## ShellSort
    algo = "ShellSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(shellSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append([algo, 0, 0,
                f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
                f"Theoretisch:{SUFFIX}\nAverage Case: O(n log n)\nWorst Case: ~O(n²)"])

    ### Stabile Sortierverfahren
    ## BubbleSort
    algo = "BubbleSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(bubbleSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append(
        [algo, 0, 0,
         f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
         f"Theoretisch:{SUFFIX}\nBest Case: O(n)\nAverage Case: O(n²)\nWorst Case: O(n²)"])

    ## InsertionSort
    algo = "InsertionSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(insertionSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append(
        [algo, 0, 0,
         f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
         f"Theoretisch:{SUFFIX}\nBest Case: O(n)\nAverage Case: (n²)\nWorst Case: O(n²)"])

    ## MergeSort
    algo = "MergeSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    index += 1
    best, _ = big_o.big_o(mergeSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append([algo, 0, 0, f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}"
                            f"Theoretisch:{SUFFIX} O(n log n)"])

    ## RadixSort
    algo = "RadixSort"
    benchmarkStatus = f"Bench {algo}... ({index}/8)"
    best, _ = big_o.big_o(radixSort, lambda n: big_o.datagen.integers(n, 0, maximum ** 2), max_n=maximum)
    tbl.append(
        [algo, 0, 0, f"{UNDERLINEPREFIX}Gemessen:{SUFFIX} {O(best)}\n{UNDERLINEPREFIX}Theoretisch:{SUFFIX} O(l*n)"])

    benchmarkStatus = "Done benchmarking."
    benchmarkDone = True

    while not demoDone:
        time.sleep(0)

    for algo in "QuickSort,HeapSort,SelectionSort,ShellSort,BubbleSort,InsertionSort,MergeSort,RadixSort".split(','):
        idx = next(i for i, row in enumerate(tbl) if row[0] == algo)
        tbl[idx][1] = max([demoLog[algo]["Dauer"][x] for x in demoLog[algo]["Dauer"].keys()])
        demoLog[algo]["Dauer"] = {k: v for k, v in demoLog[algo]["Dauer"].items() if v != 0}
        tbl[idx][2] = min([demoLog[algo]["Dauer"][x] for x in demoLog[algo]["Dauer"].keys()])

    tbl = sorted(tbl, key=lambda t: t[2])  # Sort by besttime
    tbl[0][0] = GREENPREFIX + tbl[0][0] + SUFFIX
    tbl[-1][0] = REDPREFIX + tbl[-1][0] + SUFFIX

    benchmark = tbl
    benchmark = sorted(benchmark, key=lambda t: t[2])  # Sort by besttime
    benchmarkHeader = header


def demo():
    global demoLog, demoHeader, demoTbl, demoDone, benchmarkDone
    skipBubbleSort = False
    iteration = 0
    demoLog.update({
        "QuickSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "HeapSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "SelectionSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "ShellSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "BubbleSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "InsertionSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "MergeSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        },
        "RadixSort": {
            "Dauer": {},
            "Benchmark": {},
            "Iterationen": {},
            "Komplexität": None
        }
    })
    for round in range(0, 100):

        maxTime = (round + 1) * 12 ** 2
        arr = [randint(0, maxTime * 2) for x in range(0, maxTime)]

        ### Instabile Sortierverfahren
        ## Quicksort
        t0 = datetime.now()
        quickSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["QuickSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["QuickSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)

        demoTbl.append(["QuickSort", len(arr), delta.microseconds])

        ## Heapsort
        t0 = datetime.now()
        heapSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["HeapSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["HeapSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["HeapSort", len(arr), delta.microseconds])

        ## SelectionSort
        t0 = datetime.now()
        selectionSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["SelectionSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["SelectionSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["SelectionSort", len(arr), delta.microseconds])

        ## ShellSort
        t0 = datetime.now()
        shellSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["ShellSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["ShellSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["ShellSort", len(arr), delta.microseconds])

        ### Stabile Sortierverfahren
        if not skipBubbleSort:
            ## BubbleSort
            t0 = datetime.now()
            bubbleSort(arr, demoLog, iteration, round)
            delta = datetime.now() - t0
            demoLog["BubbleSort"]["Dauer"][f"{round}"] = delta.microseconds
            demoLog["BubbleSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
            demoTbl.append(["BubbleSort", len(arr), delta.microseconds])
            if delta.seconds > 20:
                demoStatus = f"Skipping BubbleSort. Duration ({delta}) to high."
                skipBubbleSort = True
        else:
            demoTbl.append(["BubbleSort", len(arr), "Skipped"])

        ## InsertionSort
        t0 = datetime.now()
        insertionSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["InsertionSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["InsertionSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["InsertionSort", len(arr), delta.microseconds])

        ## MergeSort
        t0 = datetime.now()
        mergeSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["MergeSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["MergeSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["InsertionSort", len(arr), delta.microseconds])

        ## RadixSort
        t0 = datetime.now()
        radixSort(arr, demoLog, iteration, round)
        delta = datetime.now() - t0
        demoLog["RadixSort"]["Dauer"][f"{round}"] = delta.microseconds
        demoLog["RadixSort"]["Benchmark"][f"{round}"] = delta.microseconds / len(arr)
        demoTbl.append(["RadixSort", len(arr), delta.microseconds])
        demoTbl = sorted(demoTbl, key=lambda t: t[2])  # Sort by besttime
        demoTbl[0][0] = GREENPREFIX + demoTbl[0][0] + SUFFIX
        demoTbl[-1][0] = REDPREFIX + demoTbl[-1][0] + SUFFIX
        while len(demoTbl) != 0:
            time.sleep(0)
        if benchmarkDone:
            break
    demoDone = True


if __name__ == "__main__":
    # Create Threads
    threads = [threading.Thread(target=benchmarkTask), threading.Thread(target=demo)]
    for t in threads:
        t.start()

    while threads[0].is_alive() or threads[1].is_alive():
        if len(demoTbl) == 8 and threads[1].is_alive() and threads[0].is_alive():
            print(f"{BOLDPREFIX}{MAGENTAPREFIX}[BENCHMARK]{YELLOWPREFIX}[INFO]{SUFFIX + SUFFIX} {benchmarkStatus}\n")
            print(
                f"{BOLDPREFIX}{MAGENTAPREFIX}[DEMO]{YELLOWPREFIX}[INFO]{SUFFIX + SUFFIX}\n{tabulate(demoTbl, demoHeader)}\n")
            demoTbl.clear()
        elif threads[0].is_alive() and not threads[1].is_alive():
            print(f"{BOLDPREFIX}{MAGENTAPREFIX}[BENCHMARK]{YELLOWPREFIX}[INFO]{SUFFIX + SUFFIX} {benchmarkStatus}\n")
        elif threads[1].is_alive() and not threads[0].is_alive() and len(demoTbl) == 8:
            print(
                f"{BOLDPREFIX}{MAGENTAPREFIX}[DEMO]{YELLOWPREFIX}[INFO]{SUFFIX + SUFFIX}\n{tabulate(demoTbl, demoHeader)}\n")
            demoTbl.clear()

    ## Ausgabe
    print(tabulate(benchmark, benchmarkHeader, "rounded_grid"))
