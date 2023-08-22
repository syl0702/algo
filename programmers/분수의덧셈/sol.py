import math
def solution(numer1, denom1, numer2, denom2):
    answer = []

    ds = denom1 * denom2
    nums = numer1 * denom2 + numer2 * denom1
    gcd = math.gcd(nums, ds)
    if gcd != 1:
        nums = nums // gcd
        ds = ds // gcd
        answer = [nums, ds]
    else:
        answer = [nums, ds]
    return answer

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))