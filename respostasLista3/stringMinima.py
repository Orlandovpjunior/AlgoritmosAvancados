s = list(input())

melhor = ['z'] * len(s)
melhor[-1] = s[-1]
for i in range(len(s) - 2, -1, -1):
    melhor[i] = min(s[i], melhor[i + 1])

t = []
u = [] 

for i in range(len(s)):
    while t and t[-1] <= melhor[i]:
        u.append(t.pop())
    if s[i] == melhor[i]:
        u.append(s[i])
    else:
        t.append(s[i])
while t:
    u.append(t.pop())
    
print("".join(u))