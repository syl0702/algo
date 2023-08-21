from itertools import *
def check(a, b, c):
    t_sum = a+b+c
    for i in range(2, t_sum):
        if t_sum % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    l_num = list(combinations(nums, 3))
    for l in l_num:
        # temp.append(sum(l))
        if check(l[0], l[1], l[2]):
            answer += 1
    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))