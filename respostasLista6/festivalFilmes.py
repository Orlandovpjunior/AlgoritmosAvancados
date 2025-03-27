n = int(input())

filmes = []

for _ in range(n):
    start, end = map(int, input().split())
    filmes.append((start, end))

filmes.sort(key=lambda x: x[1])

contador = 0
fim_ultimo_filme = 0

for start, end in filmes:
    if start >= fim_ultimo_filme:
        contador += 1
        fim_ultimo_filme = end

print(contador)
