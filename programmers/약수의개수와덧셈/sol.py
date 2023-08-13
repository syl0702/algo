def solution(left, right):
    answer = 0
    s1 = list(range(left, right+1))
    for n in s1:
        for i in range(1, right):
            if n ** 0.5 == i:
                n == -(n)
                answer = sum(s1)
    


    return answer

print(solution(13, 17))
print(solution(24, 27))