def solution(s):
    for i in range(len(s)):
        answer = str.title(s)
        if s[i].isdigit():
            s[i+1] = str.lower()
        
    # answer = ''
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))