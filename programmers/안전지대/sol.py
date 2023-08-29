def solution(board):
    temp = []
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                temp.append((i,j))

    for row, col in temp:
        for n in range(8):
            nrow = row + dx[n]
            ncol = col + dy[n]
            if 0 <= nrow < len(board) and 0 <= ncol < len(board):
                board[nrow][ncol] = 1

    answer = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                answer += 1
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))