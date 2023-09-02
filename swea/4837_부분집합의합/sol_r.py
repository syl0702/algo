import sys
from itertools import combinations
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())
temp = []
for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))
    count = 0
    temp = list(combinations(numbers, N))
    for t in temp:
        if sum(t) == K:
            count += 1
    
    print(count)
