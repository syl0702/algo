def solution(quiz):
    answer = []
    for q in quiz:
        t = q.split('=')
        z = eval(t[0])
        if z == int(t[-1]):
            answer += 'O'
        else:
            answer += 'X'
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))