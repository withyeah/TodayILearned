import sys
sys.stdin = open('forth_input.txt')

def calculate(data):
    global stack, operator
    for i in data:
        if i == '.':
            if len(stack) > 1:
                return 'error'
            else:
                return stack[-1]
        elif i in operator and len(stack) < 2:
            return 'error'
        elif i not in operator:
            stack.append(i)
        else:
            if i == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == '*':
                stack.append(int(stack.pop())*int(stack.pop()))   
            elif i == '-':
                stack.append(-int(stack.pop())+int(stack.pop()))
            elif i == '/':
                stack.append(int(1/int(stack.pop())*int(stack.pop())))

T = int(input())
for tc in range(T):
    data = input().split()
    stack = []
    operator = '+-*/'
    print(f'#{tc+1} {calculate(data)}')