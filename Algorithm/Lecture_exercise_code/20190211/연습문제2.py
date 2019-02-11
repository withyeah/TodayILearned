s = []

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print('Stack is Empty!')
        return
    else:
        return s.pop(-1)

def parencheck(a):
    for i in a:
        if i == '(':
            push('(')
        elif i == ')':
            ret = pop()
            if ret != '(':
                return False
    return not s

print(parencheck('()()((()))('))