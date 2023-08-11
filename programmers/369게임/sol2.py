def solution(order):
    answer = 0
    print(str(order))
    for num in str(order):
        if num in {'3', '6', '9'}:
            answer += 1
    

    # print(n) 
    return answer

print(solution(3))
print(solution(29423))