numTopicos = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sumAcum =[]

for i in range(numTopicos):
    sumAcum.append(a[i] - b[i])

sumAcum.sort()

l = 0
h = len(sumAcum) - 1
out = 0

while h > l:
    if sumAcum[h] + sumAcum[l] > 0:
        out += h - l
        h -= 1
    if sumAcum[h] + sumAcum[l] <= 0:
        l += 1

print(out)