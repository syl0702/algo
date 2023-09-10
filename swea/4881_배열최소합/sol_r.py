import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

temp = []
def minsum(idx, used, sums):
    global min_sum

    if idx == N:
        if sums < min_sum:
            min_sum = sums
        return
    if sums > min_sum:
        return
    
    for i in range(N):
        if used[i] == False:
            sums += nums[idx][i]
            used[i] = True
            minsum(idx+1, used, sums)

            sums -= nums[idx][i]
            used[i] = False




for tc in range(1, T+1):
    N = int(input())
    nums = []
    for _ in range(N):
        num = list(map(int, input().split()))
        nums.append(num)

    
    used = [False]*N

    sums = 0
    min_sum = 100000000000

    minsum(0, used, sums)

    print(f'#{tc} {min_sum}')

