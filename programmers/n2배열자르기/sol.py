def solution(n, left, right):
    answer = []
    array = [[0 for _ in range(n)] for _ in range(n)]
    # print(array)
    for i in range(1, n):
        for j in range(n):
            for k in range(n):
                array[j][k] == i
        print(array)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))