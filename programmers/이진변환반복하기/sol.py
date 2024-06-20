def solution(s):
    answer = []
    # print(int(len(s)))
    def proc(s):
        s1 = s.replace("0", "")
        s2 = bin(len(s1))
        s = s2
        return s
    
    temp = 0
    if int(s) != 1:
        proc(s)
        temp += 1
        print(s)
    else:
        temp += 1
        answer.append(temp)

    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))