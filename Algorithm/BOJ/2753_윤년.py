year = int(input())
if (not (year % 4)):
    if (year % 100) | (not (year % 400)):
        print(1)
    else:
        print(0)
else:
    print(0)
