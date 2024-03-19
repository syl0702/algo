def solution(A,B):
    answer = 0
    answer += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))
    

    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))