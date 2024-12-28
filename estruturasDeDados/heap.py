from collections import Counter
import heapq 

arr = [4, 2, 4, 6, 8, 8, 1, 3]

#min heap
def heapSort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n


    for i in range(n):
        min = heapq.heappop(arr)
        new_list[i] = min

    return new_list

#max heap
arr2 = [12,2,5,6,3,1,3,5,7,8,10]

def heapSort2(arr):
    for i in range(len(arr2)):
        arr2[i] = -arr2[i]

    heapq.heapify(arr2)
    n = len(arr2)
    new_arr = [0] * n

    for index in range(len(arr2)):
        maxx = -heapq.heappop(arr2)
        new_arr[index] = maxx
    return new_arr

# heap com frequência
D = [5,4,3,5,4,3,5,5,4]
counter = Counter(D)
heap = []
for k,v in counter.items():
    heapq.heappush(heap, (v, k))

print(heapSort(arr))
print(heapSort2(arr2))
print(heap)