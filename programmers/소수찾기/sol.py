from itertools import permutations

def quest(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    temp = list(map(int, numbers))
    perm_set = set()
    # perm = list(permutations(temp))
    # result = [''.join(map(str, p)) for p in perm]
    # result2 = list(map(int, set(result)))
    for r in range(1, len(temp)+1):
        for p in permutations(temp, r):
            number = int("".join(map(str, p)))
            perm_set.add(number)
    
    perm = list(perm_set)
    # print(perm)

    for num in perm:
        if quest(num):
            answer += 1

    
    return answer

print(solution("17"))
print(solution("011"))