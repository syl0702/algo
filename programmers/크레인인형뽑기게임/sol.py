def solution(board, moves):
    answer = 0
    temp = []
    result = []
    for j in range(len(board)):
        b = [i[j] for i in board]
        temp.append(b)
    # print(temp)
    for m in moves:
        
        for k in range(len(temp[m-1])):

            if temp[m-1][k] != 0:
                result.append(temp[m-1][k])
                temp[m-1].pop(k)
                # print(result)
                if len(result) >1:
                    if result[-1] == result [-2]:
                        answer += 2
                        result= result[:-2]
                break
                

    # while len(result) > 1:
    #     for r in range(len(result)-1):
    #         if  result[r] == result [r+1]:
    #             answer += 2
            
            
    # print(temp)
    # print(result)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))