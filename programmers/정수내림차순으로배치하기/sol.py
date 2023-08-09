def solution(n):
    answer = 0
    temp = 0
    nums = list(str(n))
    nums.sort(reverse = True)
    answer = int(''.join(nums))
    return answer

print(solution(118372))
