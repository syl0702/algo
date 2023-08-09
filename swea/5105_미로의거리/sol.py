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
                # 거리 3이 되면 도착지와 헷갈릴 수 있으므로 -1로 시작하여 갯수 센다.
                # 1과 -1~ 모두 벽으로 생각
                maze[i][j] = -1

    
    # bfs를 동작하기 위한 큐
    queue = []
    queue.append(start)

    # 상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0

    while len(queue):
        now = queue.pop(0)
        x, y = now[0], now[1]

        pprint(maze)

        # 상하좌우 방향을 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 안에 있다면 진행
            if 0<= nx < N and 0 <= ny < N:
                # print(nx, ny)
                # 길이라면
                if maze[nx][ny] == 0:
                    # 앞으로 가야 할 위치의 좌표
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] - 1
                # 도착 지점이라면
                elif maze[nx][ny] == 3:
                    # 거리 계산 결과를 저장
                    result = abs(maze[x][y]) -1
    
    pprint(result)