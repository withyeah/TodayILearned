import sys
sys.stdin = open('시간외근무수당_input.txt')

data = [list(map(float, input().split())) for _ in range(5)]
time = 0
for datum in data:
    s, e = datum
    if e - s - 1.0 >= 4:
        time += 4.0
    elif e - s - 1.0 >= 0:
        time += e - s - 1.0
    
if time <= 5:
    time *= 1.05
elif time >= 15:
    time *= 0.95
print(int(time*10000))