def solution(n):
    ans = 0
    temp = []
    # k: 점프하는 칸의 수 (최소화 해야함)
    for k in range(1, n+1):
        i = k * 2 #현위치
        if i == n //2 and n % 2 == k:
            ans += 2
        elif i == n // 2 and n % 2 == 0:
            ans += 1
        else:
            k+=1

    return ans

print(solution(5))
print(solution(6))
print(solution(5000))