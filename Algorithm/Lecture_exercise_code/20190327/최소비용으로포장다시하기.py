# def pack(ni):
#     global cnt
#     ni.sort()
#     ni.insert(0, ni.pop(0) + ni.pop(0))
#     cnt += ni[0]
#
N = int(input())
ni = list(map(int, input().split()))
cnt = 0
# while len(ni) >= 2:
#     pack(ni)
# print(cnt)

# sort 없이 단순정렬로 맨 앞 2개만 정렬해서 풀기
for k in range(N-1):
    # k 위치에서 2개씩만 정렬
    for i in range(k, k+2):
        for j in range(i+1, N):
            if ni[i] > ni[j]:
                ni[i], ni[j] = ni[j], ni[i]
    # k, k+1 번째 포장
    ni[k+1] += ni[k]
    # 포장 비용 누계
    cnt += ni[k+1]
