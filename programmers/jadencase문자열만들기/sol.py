def solution(s):
    answer = str.title(s)
    for i in range(len(s)):
        if s[i].isdigit() and i < len(s)-1:
            answer = answer[:i+1] + answer[i+1].lower() + answer[i+2:]
        
    # answer = ''
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))