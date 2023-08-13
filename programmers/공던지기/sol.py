def solution(numbers, k):
    answer = 0
    temp = []
    if len(numbers) % 2 == 0:
        players = numbers[0::2]
    else:
        players = numbers[0::2] + numbers[1::2]

    answer = players[k % len(players) -1]
    
    return answer

print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))