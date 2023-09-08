import re
def solution(new_id):
    answer = ''
    # result = ''
    new_id = new_id.lower()
    
    for n in new_id:
        if n.isalnum() or n in '-_.':
            answer += n
    # for a in range(1, len(result)):
    #     if result[a-1] != result[a]:
            
    #         answer += result[a]
    while '..' in answer:
        answer = answer.replace('..', '.')
            
    
    if answer[0] == '.' and len(answer)>1:
        answer = answer[1:]
    else:
        answer
    
    if answer[-1] == '.':
        answer = answer[:-1]
    else: answer

    if answer == '':
        answer = 'a'
    else:
        answer

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer) <= 3:
        answer = answer + answer[-1]*(3-len(answer))

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))