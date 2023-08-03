import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for i in range(T+1):
    N = int(input())

    board = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        # [2, 2, 4, 4, 1] => r1, c1, r2, c2, color
        color_data = list(map(int, input().split()))
        
        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        # 색칠시작
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color
    pprint(board)

    count = 0

    for x in range(board):
        for y in range(board[0]):
            if board[x][y] == 3:
                count += 1
