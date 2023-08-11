def solution(n):
    answer = 0
    for i in range(max(n, 6), n*6+1):
        if i % n == 0 and i % 6 == 0:
            answer = int(i/6)
            return answer

print(solution(6))
print(solution(10))
print(solution(4))