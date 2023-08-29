def solution(dartResult):
    answer = 0
    dartResult = dartResult.replace('10', 'a')
    temp = []

    for d in dartResult:
        if d.isdigit() or d == 'a':
            if d == 'a':
                temp.append(10)
            else:
                temp.append(int(d))
        elif d == 'S':
            n = temp.pop()
            temp.append(n**1)
        elif d == 'D':
            n = temp.pop()
            temp.append(n**2)
        elif d == 'T':
            n = temp.pop()
            temp.append(n**3)
        elif d == '*':
            n = temp.pop()
            if len(temp) >0:
                temp[-1]*= 2
            temp.append(n*2)
        elif d == '#':
            n = temp.pop()
            temp.append(n*(-1))
    answer = sum(temp)
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))