def backtrack(s, path, used, resultados):
    if len(path) == len(s):
        resultados.add(''.join(path)) 
        return

    for i in range(len(s)):
        if used[i]:
            continue
        used[i] = True
        path.append(s[i])
        backtrack(s, path, used, resultados)
        path.pop()
        used[i] = False

s = input().strip()
s = sorted(s)

used = [False] * len(s)
resultados = set()
backtrack(s, [], used, resultados)

resultados_ordenados = sorted(resultados)
print(len(resultados_ordenados))
for r in resultados_ordenados:
    print(r)
