# ==============================
# KODE TUGAS: PBL0601
# ==============================
# Algoritma dan Kode Program Sorting:
# 1. Shell Sort
# 2. Merge Sort
# 3. Quick Sort
# Data: [40, 35, 82, 80, 8, 13, 59]
# ==============================

import time

global step
step = 0

# ==============================
# SHELL SORT
# ==============================
def shell_sort(arr):
    global step
    n = len(arr)
    gap = n // 2
    print('\n=============================')
    print('SHELL SORT')
    print('=============================')
    print('List awal:', arr)
    time.sleep(1)
    print('Memulai proses pengurutan dengan Shell Sort ...')
    time.sleep(1)
    print('___________________________________________')

    while gap > 0:
        print('\nGap sekarang =', gap)
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                step += 1
                print('\nLangkah ke-', step)
                print('Urutannya:', arr)
                print('Perbandingan:', arr[j-gap], 'dan', temp)
                print('Karena', arr[j-gap], 'lebih besar dari', temp, '→ dilakukan SWAP')
                arr[j] = arr[j - gap]
                print('List sementara:', arr)
                time.sleep(1)
                j -= gap
            arr[j] = temp
        gap //= 2
    print('\nData sudah terurutkan dengan Shell Sort.')
    print('List akhir:', arr)
    print('===========================================')
    time.sleep(2)


# ==============================
# MERGE SORT
# ==============================
def merge_sort(arr):
    global step
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            step += 1
            print('\nLangkah ke-', step)
            print('Kiri:', L)
            print('Kanan:', R)
            print('Bandingkan', L[i], 'dan', R[j])
            time.sleep(1)
            if L[i] < R[j]:
                arr[k] = L[i]
                print('Ambil', L[i], '(lebih kecil)')
                i += 1
            else:
                arr[k] = R[j]
                print('Ambil', R[j], '(lebih kecil)')
                j += 1
            k += 1
            print('List sementara:', arr)
            time.sleep(1)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# ==============================
# QUICK SORT
# ==============================
def partition(arr, low, high):
    global step
    pivot = arr[high]
    i = low - 1
    print('\nPivot =', pivot)
    for j in range(low, high):
        step += 1
        print('\nLangkah ke-', step)
        print('Urutannya:', arr)
        print('Bandingkan', arr[j], 'dengan pivot', pivot)
        if arr[j] <= pivot:
            i += 1
            print('Karena', arr[j], '<=', pivot, '→ dilakukan SWAP')
            arr[i], arr[j] = arr[j], arr[i]
        else:
            print('Tidak perlu swap.')
        print('List sementara:', arr)
        time.sleep(1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print('Tukar pivot ke posisi akhir yang benar.')
    print('List sementara:', arr)
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ==============================
# MENU UTAMA
# ==============================
def main():
    global step
    data_awal = [40, 35, 82, 80, 8, 13, 59]
    print('=====================================')
    print('  PROGRAM SORTING PBL0601')
    print('=====================================')
    print('1. Shell Sort')
    print('2. Merge Sort')
    print('3. Quick Sort')
    pilih = input('Pilih metode (1/2/3): ')
    print('___________________________________________')

    if pilih == '1':
        step = 0
        data = data_awal.copy()
        shell_sort(data)

    elif pilih == '2':
        step = 0
        data = data_awal.copy()
        print('\n=============================')
        print('MERGE SORT')
        print('=============================')
        print('List awal:', data)
        time.sleep(1)
        print('Memulai proses pengurutan dengan Merge Sort ...')
        time.sleep(1)
        print('___________________________________________')
        merge_sort(data)
        print('\nData sudah terurutkan dengan Merge Sort.')
        print('List akhir:', data)
        print('===========================================')
        time.sleep(2)

    elif pilih == '3':
        step = 0
        data = data_awal.copy()
        print('\n=============================')
        print('QUICK SORT')
        print('=============================')
        print('List awal:', data)
        time.sleep(1)
        print('Memulai proses pengurutan dengan Quick Sort ...')
        time.sleep(1)
        print('___________________________________________')
        quick_sort(data, 0, len(data) - 1)
        print('\nData sudah terurutkan dengan Quick Sort.')
        print('List akhir:', data)
        print('===========================================')
        time.sleep(2)

    else:
        print('Pilihan tidak valid!')

main()
