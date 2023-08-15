def solution(balls, share):
    answer = 0
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return factorial(n-1) * n
        
    f = 1
    for b in range(balls, balls-share, -1):
        f *= b
    
    answer = int(f / factorial(share))

    return answer

print(solution(3, 2))
print(solution(5, 3))