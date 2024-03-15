def merge(arr, start, mid, end):
    temp = [] # buat temporary array utk store data

    kiri = start # kiri
    kanan = mid + 1 # kanan

    while kiri <= mid and kanan <= end: # apakah masi dizonanya
        if arr[kiri] < arr[kanan]: # apakah array kiri < arr kanan
            temp.append(arr[kiri])
            kiri += 1

        else: # kalau kanan lebih kecil dari kiri
            temp.append(arr[kanan])
            kanan += 1

    while kanan <= end : # kanan masih ada sisa value yang blm dimasukin
        temp.append(arr[kanan])
        kanan += 1

    while kiri <= mid : # kanan masih ada sisa value yang blm dimasukin
        temp.append(arr[kiri])
        kiri += 1

    for x in range(len(temp)):
        arr[start + x] = temp[x]

def mergeSort(arr, start, end):
    if(start < end):
        mid = (start + end) // 2 #cari titik tengah

        # divider
        mergeSort(arr, start, mid) # kiri
        mergeSort(arr, mid + 1, end) # kanan

        merge(arr, start, mid, end)

def main():
    arr = [7,4,1,2,8,6,5]
    print(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)



main()