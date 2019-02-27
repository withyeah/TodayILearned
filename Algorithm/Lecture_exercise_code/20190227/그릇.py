
# data = input()


data = '()()()(((())()'
stack = []
ans = 10
for i in range(1, len(data)):
    if data[i-1] == data[i]:
        ans += 5
    else:
        ans += 10
print(ans)

