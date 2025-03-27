n = int(input())
nums = map(int, input().split())

total = sum(nums)
menor = float("inf")

def backtracking(i, soma_grupo1):
    global menor

    if i == n:
        soma_grupo2 = total - soma_grupo1
        menor = min(menor, abs(soma_grupo1 - soma_grupo2))
        return

    backtracking(i + 1, soma_grupo1)
    backtracking(i + 1, soma_grupo1 + nums[i])
    
backtracking(0,0)
print(menor)