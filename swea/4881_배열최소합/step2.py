import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

def search(idx, visited):

    if idx >= N:
        print(result)
        return

    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):
        if visited[i] == False:
            # print(idx, i, '=', numbers[idx][i])
            result.append(numbers[idx][i])
            visited[i] = True
            search(idx+1, visited)
            result.pop()
            visited[i] = False


for tc in range(1, T+1):
    N = int(input())
    
    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)


    result = []
    visited = [False] * N
    search(0, visited)
    