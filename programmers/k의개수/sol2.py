def solution(i, j, k):
    answer = 0
    temp = []
    for n in range(i, j+1):
        temp +=list(str(n))
        answer = temp.count(str(k))
    return answer