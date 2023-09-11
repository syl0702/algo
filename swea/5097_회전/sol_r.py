import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    print(numbers[M % N])

# for i in range(N)
# numbers.pop(0)
# numbers.append() 