import sys
sys.stdin = open('베이비진게임_input.txt')

def babygin(llist):
    if len(llist) >= 3:
        llist.sort()
        for i in range(len(llist)-2):
            if llist[i] == llist[i+1] == llist[i+2]: return True
        setlist = sorted(list(set(llist)))
        for i in range(len(setlist) - 2):
            if setlist[i] + 1 == setlist[i+1] and setlist[i+1] + 1 == setlist[i+2]: return True
        return False

for tc in range(int(input())):
    data = list(map(int, input().split()))
    list1 = []
    list2 = []
    for i in range(0, 11, 2):
        list1.append(data[i])
        if babygin(list1):
            print('#{} 1'.format(tc+1))
            break
        list2.append(data[i+1])
        if babygin(list2):
            print('#{} 2'.format(tc+1))
            break
    else: print('#{} 0'.format(tc+1))

