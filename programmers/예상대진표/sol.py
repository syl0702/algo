def solution(n,a,b):
    answer = 0
    temp = []
    for i in range(1, n):
        if i % 2 == 0:
            temp.append(i-1)
    print(temp)
    

    return answer

print(solution(8, 4, 7))