from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    freq = Counter(nums)
    used = Counter()
    score = 0

    for x in nums:
        y = k - x
        if freq[x] - used[x] > 0 and freq[y] - used[y] > 0:
            if x == y and freq[x] - used[x] >= 2:
                used[x] += 2
                score += 1
            elif x != y:
                used[x] += 1
                used[y] += 1
                score += 1

    print(score)
