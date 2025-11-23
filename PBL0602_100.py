import time

# Lokasi file (INI YANG BUAT "TERKONEKSI")
FILE_PATH = "random100K.txt"

def load_data():
    data = []
    with open(FILE_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                data.append(int(line))
    return data

# --------- Sorting Algorithms -------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# -------------- Timer ----------------
def measure(func, inplace=True):
    data = load_data()
    start = time.time()
    if inplace:
        func(data)
    else:
        func(data)
    end = time.time()
    return end - start

# -------------- MAIN -----------------
print("FILE TERKONEKSI KE:", FILE_PATH)
print("\n--- Mengukur waktu ---\n")

print("Bubble Sort    :", measure(bubble_sort))
print("Selection Sort :", measure(selection_sort))
print("Insertion Sort :", measure(insertion_sort))
print("Shell Sort     :", measure(shell_sort))
print("Merge Sort     :", measure(merge_sort))
print("Quick Sort     :", measure(quick_sort, inplace=False))
