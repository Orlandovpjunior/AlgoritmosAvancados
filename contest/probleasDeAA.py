t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())
    valor_max = a * b * c

    for i in range(6):
        for j in range(6 - i):
            resto = 5 - i - j
            novo_a = a + i
            novo_b = b + j
            novo_c = c + resto

            valor_atual = novo_a * novo_b * novo_c
            valor_max = max(valor_max, valor_atual)
    print(valor_max)

