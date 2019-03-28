# def fibo(n):
#     if n <= 1 or fib[n]: return fib[n]
#     else:
#         fib[n] = fibo(n-1) + fibo(n-2)
#         return fib[n]
# n = int(input())
# if n == 0 or n == 1: print(1)
# else:
#     fib = [0]*n
#     fib[0] = fib[1] = 1
#     print(fibo(n-1))

def fibonacci(N):
    a, b = 1, 0
    for i in range(N):
        a, b = b, a + b
    return b

N = int(input())
print(fibonacci(N))
