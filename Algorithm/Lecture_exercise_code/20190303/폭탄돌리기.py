import sys
sys.stdin = open('폭탄돌리기_input.txt')

k = int(input())
n = int(input())
data = [tuple(input().split()) for _ in range(n)]
stack = []
for datum in data:
    t, z = datum
    stack.append([int(t), z])
q = '12345678'
q = q[k-1:]+q[:k-1]
time = 0

def bomb():
    global time, q
    while time <= 210:
        if not stack:
            return q[0]
        t, z = stack.pop(0)
        time += t
        if time > 210:
            return q[0]
        if z == 'T':
            q = q[1:]+q[:1]
        else:
            continue
    else:
        return q[0]

print(bomb())

