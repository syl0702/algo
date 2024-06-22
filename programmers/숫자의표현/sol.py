def solution(n):
    answer = 0
    sum = 0
    for i in range(1, n+1):
        # print(i)
        sum += i
        if sum < n:
            i += 1
        elif sum > n:
            break
        else:
            answer += 1
            continue
    return answer

print(solution(15))