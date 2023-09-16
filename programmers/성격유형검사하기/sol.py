def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        score = 0
        if choices[i] >= 4:
            choices[i]= -(choices[i]-4)
        else:
            choices[i]

    temp = [0, 0, 0, 0]
    print(temp)
    for j in range(len(survey)):
        if survey[j] == 'RT' or survey[j] == 'TR':
            temp[0] += choices[j]
        elif survey[j] == 'CF' or survey[j] == 'FC':
            temp[1] += choices[j]
        elif survey[j] == 'JM' or survey[j] == 'MJ':
            temp[2] += choices[j]
        else:
            temp[3] += choices[j]


   
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))