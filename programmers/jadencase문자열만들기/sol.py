def solution(s):
    for i in s:
        if i.isdigit():
            pass
        else:
            answer = str.title(s)
    # answer = ''
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))