def solution(s):
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for i, letter in enumerate(en):
        if letter in s:
            s = s.replace(letter, str(i))
        answer = s
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))