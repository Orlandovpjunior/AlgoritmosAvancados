from queue import Queue

n, k = list(map(int, input().split()))
jogadores = list(map(int, input().split()))
q = Queue()

if k > n: print(max(jogadores))
else:
    jogador, vitorias = jogadores[0], 0
    for i in range(1, n):
        q.put(jogadores[i])
    
    while True:
        topo = q.get()
        if jogador > topo:
            q.put(topo)
            vitorias += 1
        else:
            q.put(jogador)
            jogador, vitorias = topo, 1
        
        if vitorias >= k:
            print(jogador)
            break