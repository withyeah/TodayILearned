import sys
sys.stdin = open("괄호검사_input.txt")

T = int(input())
for tc in range(T):
    data = input()
    def check(data):
        stack = []
        for i in data:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' or i == '}':
                if not stack:
                    return 0
                else:
                    popvalue = stack.pop()
                    if (i == ')' and popvalue != '(') or \
                        (i == '}' and popvalue != '{'):
                        return 0
        if stack:
            return 0
        else:
            return 1
    print(f'#{tc+1} {check(data)}')