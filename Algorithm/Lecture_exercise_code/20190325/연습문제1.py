def selectionsort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = 1
        for j in range(1+1, n):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp