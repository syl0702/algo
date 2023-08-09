import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    # dfs를 동작하기 위한 스택
    stack = []
    stack.append(start)

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0

    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        maze[x][y] = 1

        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있다면 진행
            if 0<= nx < N and 0 <= ny < N:
                # print(nx, ny)
                # 길이라면
                if maze[nx][ny] == 0:
                    stack.append((nx, ny))
                # 도착 지점이라면
                elif maze[nx][ny] == 3:
                    result = 1
                    break
    
    pprint(result)

    