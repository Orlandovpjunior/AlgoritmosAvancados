from collections import deque

qtde, tamanho = map(int, input().split())
conversas = list(map(int, input().split()))

fila = deque()
elementos_na_fila = set()

for num in conversas:
    if num not in elementos_na_fila:
        if len(fila) >= tamanho:
            removido = fila.pop()
            elementos_na_fila.remove(removido)
        
        fila.appendleft(num)
        elementos_na_fila.add(num)

print(len(fila))
print(" ".join(map(str, fila)))
