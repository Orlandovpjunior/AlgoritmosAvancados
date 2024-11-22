entrada = input()
nums = [int(x) for x in entrada.split()]

def ehPalindromo(num):
    numStr = str(num)
    for i in range(int(len(numStr)/2)):
        if numStr[i] != numStr[len(numStr) - i -1]:
            return False
    return True

count = 0

for num in range(nums[0], nums[1] + 1, 1):
    if ehPalindromo(num):
        count += 1

print(count)