def solution(A,B):
    answer = 0
    for i in range(len(A)):
        answer += min(A) * max(B)
        A.remove(min(A))
        B.remove(max(B))
        i += 1
    

    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))