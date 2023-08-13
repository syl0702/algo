def solution(bin1, bin2):
    answer = ''
    i = 0 
    i += int(bin1, 2) + int(bin2, 2)
    answer = bin(i)

    return answer [2:]

print(solution("10", "11"))
print(solution("1001", "1111"))