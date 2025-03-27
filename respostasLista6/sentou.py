n, t = map(int, input().split())
valores = list(map(int, input().split()))

total = 0
end_time = 0

for tempo in valores:
    if tempo >= end_time:
        total += t
    else:
        total += (tempo + t) - end_time
    end_time = max(end_time, tempo + t)

print(total)
