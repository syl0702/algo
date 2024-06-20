def solution(s):
    answer = []
    bcnt = 0
    zerocnt = 0
    # print(int(len(s)))
    while True:
        if s == '1':
            break
        zerocnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        bcnt += 1

    answer = [bcnt, zerocnt]
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))