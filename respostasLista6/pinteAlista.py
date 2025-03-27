n = int(input())
arr = list(map(int, input().split()))
pintados = [False] * n
moedas = 0

for i in range(n - 1, -1, -1):
    if not pintados[i]:
        moedas += 1
        poder = arr[i]
        pintados[i] = True
        for d in [-1, 1]:
            j = i + d
            if 0 <= j < n and not pintados[j] and poder > 0:
                pintados[j] = True
                poder -= 1

print(moedas)
