def solution(n):
    answer = 0
    # time error
    # if n == 1 or n ==2:
    #     answer+= 1
    # elif n== 0:
    #     answer = 0

    # else:
    #     answer += (solution(n-1) + solution(n-2)) % 1234567


    if n < 2:
        answer += n
    cache = [0 for _ in range(n+1)]
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
        answer += cache[n] % 1234567
    return answer

print(solution(3))
print(solution(5))