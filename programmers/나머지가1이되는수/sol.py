def solution(n):
    answer = 0
    min_x = 1000000000
    for x in range(1, n+1):
        if n % x == 1:
            if x < min_x:
                min_x = x
    answer = min_x

    return answer

print(solution(10))
print(solution(12))