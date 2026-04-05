import time
import random
import sys

sys.setrecursionlimit(10000)


class Metrice:
    def __init__(self):
        self.comp = 0
        self.mutari = 0

    def reset(self):
        self.comp = 0
        self.mutari = 0


def bubble_sort(arr, m):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            m.comp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                m.mutari += 1


def merge_sort(arr, m):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, m)
        merge_sort(R, m)
        i = j = k = 0
        while i < len(L) and j < len(R):
            m.comp += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            m.mutari += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            m.mutari += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            m.mutari += 1


def quick_sort(arr, low, high, m):
    if low < high:
        p = partition(arr, low, high, m)
        quick_sort(arr, low, p - 1, m)
        quick_sort(arr, p + 1, high, m)


def partition(arr, low, high, m):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        m.comp += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            m.mutari += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    m.mutari += 1
    return i + 1


def genereaza(n, tip):
    if tip == "aleator": return [random.randint(0, 1000) for _ in range(n)]
    if tip == "sortat": return list(range(n))
    if tip == "invers": return list(range(n, 0, -1))
    return []


def test():
    random.seed(42)
    dimensiuni = [100, 500, 1000]
    tipuri = ["aleator", "sortat", "invers"]
    m = Metrice()

    print(f"{'Algoritm':<12} | {'N':<5} | {'Tip':<8} | {'Timp(s)':<10} | {'Comp':<10} | {'Mutari'}")
    print("-" * 65)

    for n in dimensiuni:
        for tip in tipuri:
            data_orig = genereaza(n, tip)
            algs = [
                ("Bubble", lambda a: bubble_sort(a, m)),
                ("Merge", lambda a: merge_sort(a, m)),
                ("Quick", lambda a: quick_sort(a, 0, len(a) - 1, m))
            ]

            for nume, func in algs:
                copie = data_orig.copy()
                m.reset()
                start = time.time()
                func(copie)
                durata = time.time() - start

                print(f"{nume:<12} | {n:<5} | {tip:<8} | {durata:<10.5f} | {m.comp:<10} | {m.mutari}")


test()