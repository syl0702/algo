def solution(s):
    answer = []
    def change(s):
        # temp = 0
        s11 = s.replace('0', '')
        s22 = bin(int(s11))
        s = str(s22)
        # temp += 1
        # return
    
    # s1= s.replace('0', '')
    # s2 = int(s1)
    # s3 = str(bin(s2))
    temp = 0
    for i in range(len(s)):
        if i == '0':
            change(s)
            temp += 1
        else:
            pass
        
        answer = temp
    # print(s3)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))