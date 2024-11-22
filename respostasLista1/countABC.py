def contaABC(string, i):
    if i < 0 or i + 2 >= len(string): return 0
    if(string[i] == 'A' and string[i + 1] == 'B' and string[i + 2] == 'C'): return 1
    else: return 0
    
quantidades = input()
n, q = map(int, quantidades.split())

l = list(input().strip())

abc_count = sum(contaABC(l, i) for i in range(n - 2))

for i in range(q):
    entrada = input().split()
    num = int(entrada[0]) - 1
    caracter = entrada[1]

    for i in range(num - 2, num + 1):
        abc_count -= contaABC(l, i)
    
    l[num] = caracter
    
    for i in range(num -2, num + 1):
        abc_count += contaABC(l, i)

    print(abc_count)



