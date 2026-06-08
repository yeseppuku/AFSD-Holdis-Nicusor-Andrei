import time
import random
import sys

# Crestem limita de recursivitate pentru Quick Sort pe cazurile nefavorabile
sys.setrecursionlimit(20000)

class Metrice:
    def __init__(self):
        self.comp = 0
        self.mutari = 0

    def reset(self):
        self.comp = 0
        self.mutari = 0


# --- ALGORITMI DE SORTARE ---

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
            if L[i] <= R[j]:  # S-a pus <= pentru stabilitate
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


# --- GENERAREA DATELOR DE TEST ---

def genereaza(n, tip):
    if tip == "aleator": 
        return [random.randint(0, 10000) for _ in range(n)]
    if tip == "sortat": 
        return list(range(n))
    if tip == "invers": 
        return list(range(n, 0, -1))
    if tip == "duplicate": 
        # Genereaza doar din 5 valori posibile pentru a avea multe duplicate
        return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    if tip == "aproape sortat":
        arr = list(range(n))
        # Interschimbam ~5% din elemente pentru a-l face "aproape sortat"
        for _ in range(max(1, n // 20)):
            idx1 = random.randint(0, n - 1)
            idx2 = random.randint(0, n - 1)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        return arr
    return []


# --- VERIFICAREA CORECTITUDINII ---

def este_sortat(arr):
    """Verifica daca o lista este sortata crescator."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# --- SUITA DE TESTARE ---

def test():
    # Fixam seed-ul pentru reproductibilitate
    random.seed(42)
    
    # Cerință: minimum 5 dimensiuni diferite
    dimensiuni = [100, 500, 1000, 3000, 5000] 
    
    # Cerință: minimum 5 tipuri de intrări
    tipuri = ["aleator", "sortat", "invers", "duplicate", "aproape sortat"]
    
    # Cerință: Număr de rulări per test pentru a face media (recomandat 3 sau 5)
    NUMAR_RULARI =
