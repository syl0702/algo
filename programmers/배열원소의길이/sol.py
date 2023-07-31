def solution(strlist):
    answer = []
    for strs in strlist:
        answer.append(len(strs))
    return answer
    
print(list(solution(["We", "are", "the", "world!"])))