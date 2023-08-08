import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # 직접 M번 반복
    # for _ in range(M):
    #     data = numbers.pop(0)
    #     numbers.append(data)
    # print(numbers[0])

    remain = M % N

    print(numbers[remain])