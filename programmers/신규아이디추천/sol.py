import re
def solution(new_id):
    answer = ''
    result = ''
    new = new_id.lower()
    for n in new:
        if n.isalnum() or n in '-_.':
            result += n
    for a in range(1, len(result)):
        if result[a-1] != result[a]:
            answer += result[a]
    index = answer.find('.')
    if index == -1:
        answer[:-1]
    elif index == 0:
        answer[0:]

                
                


    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))