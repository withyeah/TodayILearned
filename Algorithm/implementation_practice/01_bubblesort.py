def bubblesort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [55, 78, 7, 12, 42]
bubblesort(data)
print(data)
