def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (i << j) else "0"
    print(output)

# for i in range(-5, 6):
#     print("%3d = " % i, end='')
#     Bbit_print(i)

a = 0x86
key = 0xAA

print("a      ==> ", end="")
Bbit_print(a)

print("a^=key ==> ", end="")
a^= key
Bbit_print(a)

print("a^=key ==> ", end="")
a^= key
Bbit_print(a)