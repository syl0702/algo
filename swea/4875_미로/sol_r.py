import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    temp = []
    temp.append(start)

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    while len(temp):
        now = temp.pop()
        x = now[0]
        y = now[1]

        maze[x][y] = 1
        result = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 0:
                    temp.append((nx, ny))
                elif maze[nx][ny] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')
