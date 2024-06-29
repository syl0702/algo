import math
from collections import deque
def lcm(a,b):
    return a*b / math.gcd(a,b)
def solution(arr):
    answer = 0
    # arr = deque(arr)
    temp = []
    temp.append(lcm(arr[0], arr[1]))
    for a in range(len(arr)-2):
        arr[a] = lcm(arr[a], arr[a+1])
        a+=1
    answer += arr[a]
    # while len(arr) > 1:
    #     temp.append(lcm(arr[0], arr[-1]))
    #     arr.pop()
    #     arr.popleft()

    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))