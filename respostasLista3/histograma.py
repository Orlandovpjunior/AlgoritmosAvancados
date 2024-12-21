def maiorArea(alturas):
    pilha = []
    maxArea = 0

    for i, h in enumerate(alturas):
        comeco = i
        while pilha and pilha[-1][1] > h:
            index, height = pilha.pop()
            maxArea = max(maxArea, height * (i - index))
            comeco = index
        pilha.append((comeco, h))

    for i, h in pilha:
        maxArea = max(maxArea, h * (len(alturas) - i))
    
    return maxArea

while True:
    entrada = input()
    if entrada == '0':
        break
    else:
        nums = [int(x) for x in entrada.split()]
        n = nums[0]
        alturas = nums[1:]
        print(maiorArea(alturas))
