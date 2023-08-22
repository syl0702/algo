def solution(num, total):
    answer = []
    if total % num == 0:
        t = total // num
        answer = list(range(t-(num//2), t+(num//2)+1))
    else:
        t = total // num
        answer = list(range(t-(num//2)+1, t+(num//2)+1))
    return answer

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))