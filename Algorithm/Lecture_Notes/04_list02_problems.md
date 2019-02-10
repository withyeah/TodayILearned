# Algorithm03



[sum](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV13_BWKACUCFAYh&solveclubId=AWhKdvi6ECkDFAS6&problemBoxTitle=1%EC%9B%94+21%EC%9D%BC&problemBoxCnt=1&probBoxId=AWhvb2-6-kgDFARa&&&&&)

다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

```python
import sys
sys.stdin = open("input.txt")

for a in range(10):
    tc = int(input())
    arr = [[[0] for c in range(100)] for d in range(100)]
    for b in range(100):
        arr[b] = list(map(int, input().split()))
    maxnum = 0
    for i in range(len(arr)):
        tempsum = 0
        for j in range(len(arr[i])):
            tempsum += arr[i][j]
            if tempsum > maxnum:
                maxnum = tempsum
    for i in range(len(arr)):
        tempsum = 0
        for j in range(len(arr[i])):
            tempsum += arr[j][i]
            if tempsum > maxnum:
                maxnum = tempsum
    tempsum = 0
    for i in range(100):
        tempsum += arr[i][i]
        if tempsum > maxnum:
                maxnum = tempsum
    for i in range(99, -1, -1):
        tempsum = 0
        for j in range(len(arr[i])):
            tempsum += arr[i][j]
            if tempsum > maxnum:
                maxnum = tempsum
    print(f'#{tc} {maxnum}')
```

