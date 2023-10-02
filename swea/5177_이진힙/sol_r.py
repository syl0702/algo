import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    heap = [0]*(N+1)
    n = 0

    for i in range(N):
        n += 1
        heap[n] = numbers[i]
        child = n
        parent = child // 2

        while parent and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]

            child = parent
            parent = child // 2
    
    print(heap)

    node = N // 2
    total = 0

    while node:
        total += heap[node]
        node //= 2
    
    print(total)
    