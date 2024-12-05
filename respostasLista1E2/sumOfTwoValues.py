n, x = map(int, input().split())
arr = list(map(int, input().split()))


indexed_arr = [(arr[i], i + 1) for i in range(n)]
indexed_arr.sort()

left = 0
right = n - 1

while left < right:
    somaAtual = indexed_arr[left][0] + indexed_arr[right][0]
    if somaAtual == x:
        print(indexed_arr[left][1], indexed_arr[right][1])
        break
    elif somaAtual < x:
        left += 1
    elif somaAtual > x:
        right -= 1

else:
    print("IMPOSSIBLE")