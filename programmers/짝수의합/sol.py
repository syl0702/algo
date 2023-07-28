def solution(n):
    num = 0
    for i in range(n + 1):
        if i % 2 ==0:
            num += i
        else:
            pass
    answer = num
    return answer

print(solution(10))
print(solution(4))

# 강사님 풀이
def solution(n):
    answer = 0

    for i in range(n + 1):
        if i % 2 == 0:
            answer += i

    return answer

# 두번째 방법
def solution(n):
    answer = []

    for i in range(n+1):
        if i % 2 == 0:
            answer.append(i)
    
    
    return sum(answer)

# 간단한 방법
def solution(n):
    
    answer = range(2, n+1, 2)
    
    return sum(answer)