import sys
sys.stdin = open('반나누기_input.txt')

def seperate(data):
    global N, Min, Max, mindiff
    if Min * 3 > N: return -1
    elif Max * 3 < N: return -1
    data2 = list(set(data))
    score = {i:data.count(i) for i in data2}
    # print(score)
    for i in range(1, len(data2)-1):
        for j in range(i+1, len(data2)):
            Class[0], Class[1], Class[2] = data2[:i], data2[i:j], data2[j:]
            print(Class)
            countClass = [0, 0, 0]
            for k in range(3):
                for l in Class[k]:
                    countClass[k] += score[l]
            # print(countClass)
            if countClass[0] < Min: return -1
            elif countClass[2] > Max: return -1
            if mindiff > max(countClass) - min(countClass):
                mindiff = max(countClass) - min(countClass)
    return mindiff

T = int(input())
for tc in range(T):
    N, Min, Max = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    Class = [[], [], []]
    mindiff = 1000
    # print(seperate(data))
    seperate(data)
    print()