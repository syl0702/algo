def solution(M, N):
    answer = 0
    if M == N == 1:
        answer = 0

    elif M >= N:
        a = (N-1)*M + (M-1)
        answer += a

    elif M < N:
        a = (M-1)*N + (N-1)
        answer+= a
        
    
    return answer

print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))