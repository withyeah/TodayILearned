def aToh(c):
   if c <= '9':
       return ord(c) - ord('0')
   else:
       return ord(c) - ord('A') + 10

def makeT(x):
   for i in range(4):
       t.append(asc[x][i])

asc = [[0,0,0,0], #0
       [0,0,0,1], #1
       [0,0,1,0], #2
       [0,0,1,1], #3
       [0,1,0,0], #4
       [0,1,0,1], #5
       [0,1,1,0], #6
       [0,1,1,1], #7
       [1,0,0,0], #8
       [1,0,0,1], #9
       [1,0,1,0], #A
       [1,0,1,1], #B
       [1,1,0,0], #C
       [1,1,0,1], #D
       [1,1,1,0], #E
       [1,1,1,1]] #F

password = [[0,0,1,1,0,1], #0
            [0,1,0,0,1,1], #1
            [1,1,1,0,1,1], #2
            [1,1,0,0,0,1], #3
            [1,0,0,0,1,1], #4
            [1,1,0,1,1,1], #5
            [0,0,1,0,1,1], #6
            [1,1,1,1,0,1], #7
            [0,1,1,0,0,1], #8
            [1,0,1,1,1,1]] #9
t = []
arr = "0269FAC9A0"

for i in range(len(arr)):
   makeT(aToh(arr[i]))

# print(t)

answer = []
for i in range(len(t)-1, -1, -1):
    if t[i] == 1:
        start = i
        break
# print(t)

while len(t) >= 6:
    answer.append(t[start-5:start+1])
    t = t[:start-5]
    start = len(t) - 1
answer = reversed(answer)

ansans = []
for i in answer:
    for j in range(len(password)):
        if i == password[j]:
            ansans.append(j)
print(ansans)

