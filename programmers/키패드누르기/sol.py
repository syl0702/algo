def solution(numbers, hand):
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            answer += 'N'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))