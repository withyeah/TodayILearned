# 20190403 에서 풀다 말아서 다시 품

import sys
sys.stdin = open('상자포장하기_input.txt')

def box(no, Abox, Bbox, hap):
    global sol
    if no >= N:
        if sol < hap: sol = hap
        return
    
    # 박스를 A가 가져가는 경우
    if data[no] < Abox:
        box(no + 1, data[no], Bbox, hap + data[no])
    # 박스를 B가 가져가는 경우
    if data[no] > Bbox:
        box(no + 1, Abox, data[no], hap + data[no])
    # 박스를 아무도 가져가지 않는 경우
    box(no + 1, Abox, Bbox, hap)

# main ----------------------------
T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sol = 0
    box(0, 1000, 0, 0)
    print(sol)