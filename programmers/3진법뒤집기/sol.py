def solution(n):
    answer = 0
    three_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        three_base += str(mod)
    print(three_base)
    answer = int(three_base, 3)
    return answer

print(solution(45))
print(solution(125))