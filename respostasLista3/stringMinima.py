s = list(input())
t = []
u = []

while s or t:
    if not t:
        t.append(s.pop(0))
    elif not s or t[-1] <= s[0]:
        u.append(t.pop())
    else:
        t.append(s.pop(0))

print("".join(u)) 