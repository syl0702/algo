def solution(numbers):
    alph_num = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for key, value in enumerate(alph_num):
            numbers = numbers.replace(value, str(key))
            
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))