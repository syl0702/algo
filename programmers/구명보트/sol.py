def solution(people, limit):
    answer = 0
    people.sort()
    i = 0 # 시작 인덱스
    # print(people)
    # for p in range(len(people)-1):
    #     print(people[p])
    # if people[0] + people[1] <= limit:
    #     answer += 1
    #     for p in range(2, len(people)):
    #         if people[p] + people[p+1] <= limit:
    #             answer += 1
    #             continue
    #         else:
    #             answer += len(people) - (p+1)
    #             break
            
    # else:
    #     answer += len(people)
    while i < len(people):
        if i < len(people)-1 and people[i] + people[i+1] <= limit:
            answer += 1
            i += 2
        else:
            answer += 1
            i += 1

    # for p in range(len(people)-1):
    #     if p >= len(people):
    #         break
    #     if p < len(people)-1 and people[p] + people[p+1] <= limit:
    #         answer+=1
    #         p+=2
            
    #     else:
    #         answer += 1
    #         p+=1
            
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))