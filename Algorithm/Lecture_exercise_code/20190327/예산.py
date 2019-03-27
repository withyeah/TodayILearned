import sys
sys.stdin = open('input.txt')

def binSearch(s, e):
    m = (s + e)//2
    sol = -1
    while s <= e:
        if check(m): # limit 올리기
            sol = m
            s = m + 1
            m = (s + e)//2
        else: # limit 내리기 
            e = m - 1
            m = (s + e)//2
    return sol

def check(limit):
    global budget
    cnt = 0
    for city in data:
        if city <= limit: cnt += city
        else: cnt += limit
    if cnt <= budget: return True
    else: return False

N = int(input())
data = list(map(int, input().split()))
budget = int(input())
if sum(data) <= budget: print(max(data))
else: print(binSearch(min(data), max(data)))
