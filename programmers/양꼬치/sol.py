def solution(n, k):
    
    if n >= 10:
        answer = (n * 12000) + ((k- (n // 10)) * 2000)

    else:
        answer = (n * 12000) + (k * 2000)

    return answer

print(solution(10, 3))
print(solution(64, 6))

# 강사님 답안
def solution(n, k):
    service = n // 10
    
    answer = (n *  12000) + (k-service) * 2000

    return answer