def recursivefibo(n):
    if n <= 1: return n
    else:
        return recursivefibo(n-1) + recursivefibo(n-2)

print(recursivefibo(7))