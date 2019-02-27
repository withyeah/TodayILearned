# data = int(input())
data = 100
if data % 10:
    print(-1)
else:
    A = data//300
    data -= A*300
    B = data//60
    data -= B*60
    C = data//10
    print(A, B, C)
