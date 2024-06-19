def solution(s):
    answer = []
    def change(s):
        # temp = 0
        s11 = s.replace('0', '')
        s22 = bin(int(s11))
        s33 = int(s22, 2)
        print(s33)
        return s33
        # temp += 1
        # return
    
    # s1= s.replace('0', '')
    # s2 = int(s1)
    # s3 = str(bin(s2))
    temp = 0
    for i in range(len(s)):
        if len(s) != 1 & s[i] == '0':
            change(s)
            temp += 1
        
        elif len(s) ==1 & s[i] == 's':
            answer.append(temp)
        else:
            pass
        
    answer.append(temp)
    # print(s3)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))