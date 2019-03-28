def recursivesum(n):
    global sum
    if n <= 1: return n
    sum += n
    return n + recursivesum(n-1)

n = int(input())
sum = 0
print(recursivesum(n))