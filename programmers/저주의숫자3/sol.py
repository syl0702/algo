def solution(n):
    answer = 0
    for num in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1

    return answer

# 왜 if를 썼을 때는 답이 각각 22, 61이 나오고 while 문에서는 25, 76이 나오는 거지...
# if answer % 3 == 0 or '3' in str(answer):
    # answer += 1
print(solution(15))
print(solution(40))