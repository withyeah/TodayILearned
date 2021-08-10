n, m = map(int, input().split())
answer = []
for i in range(n):
    answer.append(min(list(map(int, input().split()))))
print(max(answer))
