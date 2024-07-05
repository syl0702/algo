def solution(n):
    answer = 0
    temp = []
    dp = [[0]*(n+1) for _ in range(n+1)]
    while n > 0:
        if n > 2:
            temp.append(2)
            n = n-2
        elif n == 2:
            temp.append(2)
            n = n-2
        else:
            temp.append(1)
            n = n - 1
    print(temp)
    return answer

print(solution(4))
print(solution(3))