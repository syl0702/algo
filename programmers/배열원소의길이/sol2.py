def solution(strlist):
    answer = []
    for strs in strlist:
        answer.append(len(strs))
    return list(answer)

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))