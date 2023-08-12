def solution(before, after):
    answer = 0
    b = sorted(list(before))
    a = sorted(list(after))
    # print(b, a)
    if b == a:
        answer = 1
    else:
        answer = 0
    return answer

print(solution("olleh", "hello"))
print(solution("allpe", "apple"))