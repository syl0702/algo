def solution(name):
    answer = 0
    temp = []
    for n in name:
        temp.append(ord(n)-65)
    

    temp.append(len(temp))
    print(temp)
    return answer

print(solution("JEROEN"))
print(solution("JAN"))