def solution(n):
    ans = 0
    temp = []
    # k: 점프하는 칸의 수 (최소화 해야함)
    for k in range(1, n+1):
        i = k * 2
        if n % 2 == k:
            ans += k
            if n // 2 == i or n//2 == i + k:
                ans += k

    return ans

print(solution(5))
print(solution(6))
print(solution(5000))