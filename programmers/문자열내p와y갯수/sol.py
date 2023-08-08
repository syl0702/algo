def solution(s):
    answer = True
    temp_s = s.lower()
    if temp_s.count('p') == temp_s.count('y'):
       return True
    else:
        return False

print(solution("pPoooyY"))
print(solution("Pyy"))