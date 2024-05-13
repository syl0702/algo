def solution(s):
    answer = []
    s1= s.replace('0', '')
    s2 = int(s1)
    s3 = str(bin(s2))
    if '0' in s3:
        s3 = s3.replace('0', '')
        
    print(s3)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))