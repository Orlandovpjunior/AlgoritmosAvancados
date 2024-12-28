import heapq

casos = int(input())

for _ in range(casos):
    tamanho = int(input())
    cartas = list(map(int, input().split()))
    
    heap = []
    poder = 0

    for num in cartas:
        if num > 0:
            heapq.heappush(heap, -num)
        elif num == 0 and heap:
            poder += -heapq.heappop(heap)

    print(poder)
