def quickSort(start, end, x):
    if start >= end:
        return
    else:
        pivot = end
        target = start

        for left in range(start, end):
            if x[left] < x[pivot]:
                x[target] , x[left] = x[left], x[target]
                target += 1

        x[target] , x[pivot] = x[pivot], x[target]
        quickSort(start, target-1, x)
        quickSort(target+1, end, x)