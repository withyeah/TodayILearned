s = "abcabcabcabcdededededede"
for i in range((len(s) // 2), 0, -1):
    size = i
    splited = [s[i:i+size] for i in range(0, len(s), size)]
    memory = ['1' + splited[0]]
    for x in range(len(splited)-1, 1, -1):
        counter = 1
        if memory[-1] == splited[x]:
            counter += 1
            memory[-1] = f'{counter}' + memory[-1]
        else:
            memory.append('1' + splited[x])
            counter = 1
print(memory)
        

