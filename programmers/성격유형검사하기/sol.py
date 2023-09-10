def solution(survey, choices):
    answer = ''
    
    for i in range(len(survey)):
        if survey[i] == 'AN':
            if choices[i] >= 4:
                choices[i] =choices[i] -3

    # for i in range(len(survey)):
    #     if choices[i] <= 4:
    #         answer += survey[i][0]
    #     else:
    #         answer += survey[i][-1]

    # while len(answer) < 5: 
    #     if 'A' or 'N' not in answer:
    #         answer+= 'A'
    #         continue
    #     if 'C' or 'F' not in answer:
    #         answer += 'C'
    #         continue
    #     if 'M' or 'J' not in answer:
    #         answer += 'J'
    #         continue
    #     if 'R' or 'T' not in answer:
    #         answer += 'R'
    #         continue

   
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))