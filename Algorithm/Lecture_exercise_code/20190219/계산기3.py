import sys
sys.stdin = open('계산기3_input.txt')

for tc in range(10):
    n = int(input())
    data = input()
    stack = []
    postfix = []
    operator = {'(': 0, '+': 1, '*': 2}
    # 중위표기식 > 후위표기식
    for i in data:
        if i.isdigit():
            postfix.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == '+' or i == '*':
                while operator[stack[-1]] >= operator[i]:
                    postfix.append(stack.pop())
                else:
                    stack.append(i)
            else:
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                else:
                    stack.pop()
    
    # 후위표기식 > 연산
    for i in postfix:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            else:
                stack.append(int(stack.pop()) * int(stack.pop()))
    print(f'#{tc+1} {stack[0]}')


                