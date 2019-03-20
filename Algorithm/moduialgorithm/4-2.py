def recursionmax(data):
    if len(data) == 1:
        return data[0]
    elif data[len(data)-1] >= data[len(data)-2]:
        del data[len(data)-2]
    else: del data[len(data)-1]
    return recursionmax(data)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(recursionmax(data))