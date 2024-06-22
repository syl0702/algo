def solution(n):
    answer = 0
    binn = str(bin(n)[2:])
    strbin = binn.count("1")
    print(strbin)
    
    return answer

print(solution(78))
print(solution(15))