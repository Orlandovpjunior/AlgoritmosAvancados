n, m = map(int,input().split())

def count_down_cards(N, M):
    if N == 1 and M == 1:
        return 1
    elif N == 1:
        return M - 2
    elif M == 1:
        return N - 2
    else:
        return (N - 2) * (M - 2)

print(count_down_cards(n, m))