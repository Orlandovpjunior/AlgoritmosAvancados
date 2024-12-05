def pode_ganhar(k, arr):
   
    alice = len(arr) - 1
    bob = 0

    while alice >= bob and k > 0:
        if arr[alice] <= k:
            alice -=1 
            bob += 1
            k -= 1
        else:
            alice -= 1
        

    if k == 0:
        return True
    else:
        return False
   

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    inicio, fim = 0, n
    maior_k = 0
    while inicio <= fim:
        mid = (inicio + fim) // 2
        if pode_ganhar(mid, arr):
            maior_k = max(mid, maior_k)
            inicio = mid + 1
        else:
            fim = mid - 1
    print(maior_k)