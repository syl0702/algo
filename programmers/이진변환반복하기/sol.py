def solution(s):
    answer = []
    def change(s):
        temp = 0
        s11 = s.replace('0')
        s22 = bin(int(s11))
        s = str(s22)
        temp += 1
        # return
    
    # s1= s.replace('0', '')
    # s2 = int(s1)
    # s3 = str(bin(s2))
    if '0' in s:
        change(s)
    else:
        pass
        
    # print(s3)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))