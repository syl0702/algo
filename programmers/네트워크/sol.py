from pprint import pprint
def solution(n, computers):
    answer = 0
    queue = []
    check_list = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            else:
                now = computers[i][j]
                
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))