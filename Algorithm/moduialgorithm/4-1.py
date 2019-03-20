def recursionsum(n):
    if n <= 1: return n
    return n + recursionsum(n-1)

print(recursionsum(3))