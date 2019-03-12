def myprint(q):
    while q:
        q -= 1
        print(' {}'.format(t[q]), end =' ')
    print()


def Perm(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            Perm(n-1, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]

t = [0] * 10
a = list(range(1, 11))
Perm(4, 3, 3)