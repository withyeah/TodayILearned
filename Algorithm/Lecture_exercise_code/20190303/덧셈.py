import sys
sys.stdin = open('덧셈_input.txt')

def plus(s, x):
    for i in range(1, len(s)):
        if int(s[:i]) + int(s[i:]) == int(x):
            return f'{int(s[:i])}+{int(s[i:])}={x}'
    return 'NONE'

for tc in range(3):
    s, x = input().split()
    print(plus(s, x))
            