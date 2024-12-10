from queue import LifoQueue

s = input()
q = LifoQueue()
ok = 1

for c in s:
    if c in '([{':
        q.put(c)
    else:
        if q.empty():
            ok = 0
            break
        f = q.get()
        if((c == ')') and f != '(') or ((c == ']') and f != '[') or ((c == '}') and f != '{'):
            ok = 0
            break

if not q.empty():
    ok = 0
if ok:
    print('S')
else:
    print('N')