def solution(n):
    answer = 0
    binn = str(bin(n)[2:])
    strbin = binn.count("1")
    # print(strbin)
    for i in range(n):
        i1 = n+i
        i2 = str(bin(i1)[2:])
        if i2.count("1") == strbin:
            answer = i1
    return answer

print(solution(78))
print(solution(15))