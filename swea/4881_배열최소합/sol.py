import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

def search(idx, visited, SUM):
    global MIN_SUM

    if idx >= N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return
    # 중간에 벌써 최솟값보다 크면 그냥 그만둬!
    if SUM > MIN_SUM:
        return

    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):
        if visited[i] == False:
            # print(idx, i, '=', numbers[idx][i])
            # result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True
            search(idx+1, visited, SUM)
            # result.pop()
            SUM -= numbers[idx][i]
            visited[i] = False


for tc in range(1, T+1):
    N = int(input())
    
    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)


    result = []
    visited = [False] * N

    SUM = 0 # 내가 바라보고 있는 숫자들의 합 넣을 것
    MIN_SUM = 100000000000


    search(0, visited, SUM)

    print(MIN_SUM) 

    
    
