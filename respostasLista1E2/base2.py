from math import pow

entrada = input()
nums = [int(x) for x in entrada.split()]

resultado = 0

for i in range(len(nums)):
    if nums[i] == 1:
        resultado += int(pow(2,i))

print(resultado)