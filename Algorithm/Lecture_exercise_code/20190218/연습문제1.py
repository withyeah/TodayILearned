str1 = '2+3*4/5'
str2 = []
operator = {'+':1, '-':1, '*':2, '/':2}
stack = []
for i in str1:
    if i not in operator:
        str2.append(i)
    else:
        if not stack:
            stack.append(i)
        else:
            if operator[i] > operator[stack[-1]]:
                stack.append(i)
            else:
                while operator[i] <= operator[stack[-1]]:
                    str2.append(stack.pop())
                stack.append(i)
if stack:
    str2.extend(stack)

print(str2)

