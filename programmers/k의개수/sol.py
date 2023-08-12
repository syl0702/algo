def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        if str(k) in str(n):
            answer += str(n).count(str(k))
    return answer

print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))