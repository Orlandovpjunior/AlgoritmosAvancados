tabuleiro = [input() for _ in range(8)]

resultado = 0
colunas = [False] * 8
diag1 = [False] * 15
diag2 = [False] * 15

def backtrack(linha):
    global resultado

    if linha == 8:
        resultado += 1
        return
    
    for coluna in range(8):
        if (tabuleiro[linha][coluna] == '.' 
            and not colunas[coluna] 
            and not diag1[linha + coluna] 
            and not diag2[linha - coluna + 7]):

            colunas[coluna] = diag1[linha + coluna] = diag2[linha - coluna + 7] = True
            backtrack(linha + 1)
            colunas[coluna] = diag1[linha + coluna] = diag2[linha - coluna + 7] = False

backtrack(0)
print(resultado)
