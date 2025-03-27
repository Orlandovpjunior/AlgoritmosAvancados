def subconjuntos(arr):
    
    resultado = []

    def backtrack(inicio, caminho):
        resultado.append(caminho[:])

        for i in range(inicio, len(arr)):

            caminho.append(arr[i])
            backtrack(1 + i, caminho)
            caminho.pop()

    backtrack(0, [])
    return resultado
   
nums = [1, 2, 3]
subconjunto = subconjuntos(nums)

for s in subconjunto:
    print(s)

