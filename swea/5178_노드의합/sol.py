import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]

    for i in range(M):
        idx , nums = map(int, input().split())
        tree[idx] = nums

    for j in range(N, 0, -1):
        if j // 2 > 0:
            tree[j//2] += tree[j]

    print(f'#{tc} {tree[L]}')