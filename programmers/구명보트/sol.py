def solution(people, limit):
    answer = 0
    people.sort()
    # print(people)
    # for p in range(len(people)-1):
    #     print(people[p])
    if people[0] + people[1] <= limit:
        answer += 1
        for p in range(1, len(people)-2):
            if people[p] + people[p+1] <= limit:
                answer += 1
                continue
            else:
                answer += len(people) - (p+1)
            
    else:
        answer += len(people)
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))