def solve(a,b,c):
    visitados = [False] * b
    def dfs(valorAtual):

        if valorAtual == c:
            return True
        
        if visitados[valorAtual]:
            return False
        
        visitados[valorAtual] = True

        return dfs((valorAtual + a) % b)
    
    return dfs(0)

a,b,c = map(int, input().split())
print("YES" if solve(a,b,c) else "NO")

