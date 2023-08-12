def solution(array, n):
    answer = 0
    array.sort()
    # print(array)
    k = 1000
    for num in array:
        if abs(num - n) < k:
            k = abs(num - n)
            answer = num
    return answer

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))