import math
from collections import deque
def lcm(a,b):
    return a*b / math.gcd(a,b)
def solution(arr):
    answer = 0
    for i in range(arr):
        arr[i+1] = lcm(arr[i], arr[i+1])
        i+=2

    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))