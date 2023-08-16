def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    xlim = board[0]//2
    ylim = board[1]//2
    
    for key in keyinput:
        if key == "right":
            if x >= xlim:
                x = xlim
            else:
                x += 1
        elif key == "left":
            if x <= -xlim:
                x = -xlim
            else:
                x -= 1
        elif key == "up":
            if y >= ylim:
                y = ylim
            else:
                y += 1
        elif key == "down":
            if y <= -ylim:
                y = -ylim
            else:
                y -= 1
    answer = [x, y]
    # for i in range(board[0]):
    #     for j in range(board[1]):
    #         start = [0, 0]
    #         for key in keyinput:
    #             if key == "left":
    #                 board1[i][j] == board1[i-1][j]
    #             elif key == "right":
    #                 board1[i][j]= board1[i+1][j]
    #             elif key == "up":
    #                 board1[i][j] == board1[i][j+1]
    #             elif key == "down":
    #                 board1[i][j] == board[i][j-1]
    #     answer.append(board1[i][j])
    return answer

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))