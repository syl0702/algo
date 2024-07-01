import math
from math import gcd
from collections import deque
# def lcm(a,b):
#     return a*b / math.gcd(a,b)
def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = answer*i //gcd(answer, i)

    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))