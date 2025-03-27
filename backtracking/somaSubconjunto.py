
def subconjuntos(arr):
    resultado = []

    def backtracking(inicio, caminho, soma_atual):
        if soma_atual == 16:
            resultado.append(caminho[:])
            return
        
        if soma_atual > 16:
            return
            
        for i in range(inicio, len(arr)):
            caminho.append(arr[i])
            backtracking(i + 1, caminho, soma_atual + arr[i])
            caminho.pop()

    backtracking(0,[],0)
    return resultado

lista =  [2, 4, 6, 10]

subconjunto = subconjuntos(lista)

for s in subconjunto:
    print(s)


