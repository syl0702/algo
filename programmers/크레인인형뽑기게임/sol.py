def solution(board, moves):
    answer = 0
    temp = []
    for j in range(len(board)):
        b = [i[j] for i in board]
        temp.append(b)
    # print(temp)
    for m in moves:
        print(temp[m-1])

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))