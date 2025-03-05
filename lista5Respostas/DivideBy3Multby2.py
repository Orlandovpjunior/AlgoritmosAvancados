from collections import deque, defaultdict

n = int(input())
nums = list(map(int, input().split()))

grafo = defaultdict(set)
possiveis_inicio = set(nums)

for a in nums:
    for b in nums:
        if a * 2 == b or (a % 3 == 0 and a // 3 == b):
            grafo[a].add(b)
            possiveis_inicio.discard(b)

inicio = possiveis_inicio.pop()
fila = deque([inicio])
seq = []

while fila:
    no = fila.popleft()
    seq.append(no)

    for vizinhos in grafo[no]:
        fila.append(vizinhos)

print(*seq)