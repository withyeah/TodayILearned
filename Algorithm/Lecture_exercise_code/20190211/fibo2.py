# memo를 위한 리스트를 생성하고,
# memo[0] 을 0으로, memo[1]는 1로 초기화 한다

def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
print(fibo(50))
# 앞에서부터 순서대로 구해진다