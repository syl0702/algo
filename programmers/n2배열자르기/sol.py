def solution(n, left, right):
    answer = []
    array = [[0 for _ in range(n)] for _ in range(n)]
    # print(array)
    # 0만 들어간 곳에 숫자 넣기
    # 배열에 1부터 n까지 채우기
    count = 1
    for i in range(n):
        for j in range(n):
            array[i][j] = count
            count += 1
        print(array)
        arr_to_list = [item for sublist in array for item in sublist]
        print(arr_to_list)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))