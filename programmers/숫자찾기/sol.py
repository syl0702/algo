def solution(num, k):
    answer = 0
    n = list(map(int, str(num)))
    if k in n:
        answer = n.index(k) + 1
    else:
        answer = -1
    return answer

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))